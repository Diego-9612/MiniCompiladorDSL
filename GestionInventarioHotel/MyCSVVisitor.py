import pandas as pd
from antlr4 import ParseTreeVisitor
from dateutil.parser import ParserError

class CSVProcessingError(Exception):
    """Excepción personalizada para errores de procesamiento"""
    pass

class MyCSVVisitor(ParseTreeVisitor):
    def __init__(self):
        self.original_data = None
        self.filtered_data = None
        self.aggregation_result = None
        self.active_filters = []
        self._current_dataset = None  # 'original' o 'filtered'

    def visitProg(self, ctx):
        for stat in ctx.stat():
            self.visit(stat)
        return self

    def visitLoadStat(self, ctx):
        try:
            filename = ctx.STRING().getText().strip('"')
            self.original_data = pd.read_csv(filename, parse_dates=['fecha_ingreso', 'fecha_salida'])
            self.filtered_data = self.original_data.copy()
            self.active_filters = []
            print(f"\n✅ CSV cargado: {filename} ({len(self.original_data)} registros)")
        except Exception as e:
            raise CSVProcessingError(f"Error cargando CSV: {str(e)}")

    def visitFilterStat(self, ctx):
        try:
            self._current_dataset = 'original'
            new_condition = self.visit(ctx.expr())
            self.active_filters.append(new_condition)
            
            # Aplicar todos los filtros acumulativamente
            combined_condition = pd.Series(True, index=self.original_data.index)
            for cond in self.active_filters:
                aligned_cond = cond.reindex(combined_condition.index).fillna(False)
                combined_condition &= aligned_cond
                
            self.filtered_data = self.original_data[combined_condition]
            print(f"🔎 Filtro aplicado. Registros restantes: {len(self.filtered_data)}")
            
        except KeyError as e:
            raise CSVProcessingError(f"Columna {str(e)} no existe")
        except Exception as e:
            raise CSVProcessingError(f"Error aplicando filtro: {str(e)}")
        finally:
            self._current_dataset = None

    def visitAggregateStat(self, ctx):
        try:
            func = ctx.FUNC_NAME().getText()
            column = ctx.STRING().getText().strip('"')
            
            if column not in self.filtered_data.columns:
                raise CSVProcessingError(f"Columna '{column}' no encontrada")
            
            if func in ['SUM', 'AVERAGE'] and not pd.api.types.is_numeric_dtype(self.filtered_data[column]):
                raise CSVProcessingError(f"Columna '{column}' debe ser numérica")
            
            subset = self.filtered_data
            if ctx.expr():
                self._current_dataset = 'filtered'
                condition = self.visit(ctx.expr())
                subset = self.filtered_data[condition]
                print(f"🔧 Filtro WHERE aplicado. Registros usados: {len(subset)}")
            
            if func == "SUM":
                result = subset[column].sum()
            elif func == "COUNT":
                result = subset.shape[0]
            elif func == "AVERAGE":
                result = subset[column].mean()
            else:
                raise CSVProcessingError(f"Función no soportada: {func}")
            
            self.aggregation_result = result
            print(f"\n📊 Resultado de {func}({column}): {result:.2f}")
            
        except CSVProcessingError as e:
            raise
        finally:
            self._current_dataset = None

    def visitPrintStat(self, ctx):
        print("\n📄 Datos actuales:")
        print(self.filtered_data.to_string(index=False))
        print(f"\nMostrando {len(self.filtered_data)} de {len(self.original_data)} registros")

    def _get_current_data(self):
        if self._current_dataset == 'filtered' and self.filtered_data is not None:
            return self.filtered_data
        return self.original_data

    def visitLogicalExpr(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        op = ctx.LOGICAL_OP().getText()
        
        try:
            if op == "AND":
                return left & right
            return left | right
        except Exception as e:
            raise CSVProcessingError(f"Error en operación {op}: {str(e)}")

    def visitComparisonExpr(self, ctx):
        try:
            data = self._get_current_data()
            col = ctx.STRING().getText().strip('"')
            operator = ctx.OPERATOR().getText()
            value = self.visit(ctx.value())
            
            if col not in data.columns:
                raise CSVProcessingError(f"Columna '{col}' no existe")
            
            col_data = data[col]
            if isinstance(value, (int, float)) and not pd.api.types.is_numeric_dtype(col_data):
                raise CSVProcessingError(f"Columna '{col}' no es numérica")
            elif isinstance(value, str) and pd.api.types.is_numeric_dtype(col_data):
                raise CSVProcessingError(f"Columna '{col}' es numérica")
            
            if operator == "==": return col_data == value
            elif operator == "!=": return col_data != value
            elif operator == ">": return col_data > value
            elif operator == "<": return col_data < value
            elif operator == ">=": return col_data >= value
            elif operator == "<=": return col_data <= value
            
        except Exception as e:
            raise CSVProcessingError(f"Error en condición: {str(e)}")

    def visitBetweenExpr(self, ctx):
        try:
            data = self._get_current_data()
            col = ctx.STRING().getText().strip('"')
            lower = self.visit(ctx.value(0))
            upper = self.visit(ctx.value(1))
            
            if col not in data.columns:
                raise CSVProcessingError(f"Columna '{col}' no existe")
                
            col_data = data[col]
            
            # Manejar fechas
            if pd.api.types.is_datetime64_any_dtype(col_data):
                lower = pd.to_datetime(lower, errors='coerce')
                upper = pd.to_datetime(upper, errors='coerce')
                if pd.isnull(lower) or pd.isnull(upper):
                    raise CSVProcessingError("Valores de fecha inválidos en BETWEEN")
            else:
                try:
                    lower = float(lower)
                    upper = float(upper)
                except ValueError:
                    raise CSVProcessingError("Valores numéricos inválidos en BETWEEN")
            
            return col_data.between(lower, upper)
            
        except Exception as e:
            raise CSVProcessingError(f"Error en BETWEEN: {str(e)}")

    def visitValue(self, ctx):
        if ctx.NUMBER():
            num_str = ctx.NUMBER().getText()
            return float(num_str) if '.' in num_str else int(num_str)
        elif ctx.STRING():
            return ctx.STRING().getText().strip('"')