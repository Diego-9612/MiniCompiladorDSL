import pandas as pd
from antlr4 import ParseTreeVisitor

class CSVProcessingError(Exception):
    """Excepción personalizada para errores de procesamiento"""
    pass

class MyCSVVisitor(ParseTreeVisitor):
    def __init__(self):
        self.original_data = None     # Datos originales del CSV
        self.filtered_data = None      # Datos después de aplicar filtros
        self.aggregation_result = None # Resultado de agregaciones
        self.active_filters = []       # Lista de condiciones de filtro activas

    def visitProg(self, ctx):
        """Visita el programa completo ejecutando todos los comandos"""
        for stat in ctx.stat():
            self.visit(stat)
        return self

    def visitLoadStat(self, ctx):
        """Procesa el comando LOAD"""
        try:
            filename = ctx.STRING().getText().strip('"')
            self.original_data = pd.read_csv(filename)
            self.filtered_data = self.original_data.copy()
            self.active_filters = []
            print(f"\n✅ CSV cargado: {filename} ({len(self.original_data)} registros)")
        except FileNotFoundError:
            raise CSVProcessingError(f"Archivo no encontrado: {filename}")
        except Exception as e:
            raise CSVProcessingError(f"Error cargando CSV: {str(e)}")

    def visitFilterStat(self, ctx):
        """Procesa el comando FILTER con manejo de múltiples condiciones"""
        try:
            new_condition = self.visit(ctx.expr())
            self.active_filters.append(new_condition)
            
            # Aplicar todos los filtros acumulativamente
            combined_condition = pd.Series(True, index=self.original_data.index)
            for cond in self.active_filters:
                # Alinear índices y manejar valores faltantes
                aligned_cond = cond.reindex_like(combined_condition).fillna(False)
                combined_condition &= aligned_cond
                
            self.filtered_data = self.original_data[combined_condition]
            print(f"🔎 Filtro aplicado. Registros restantes: {len(self.filtered_data)}")
            
        except KeyError as e:
            print(f"❌ Error en filtro: Columna {str(e)} no existe")
            self.active_filters.pop()
        except Exception as e:
            print(f"❌ Error aplicando filtro: {str(e)}")
            self.active_filters.pop()

    def visitAggregateStat(self, ctx):
        """Procesa el comando AGGREGATE con validación de tipos"""
        try:
            func = ctx.FUNC_NAME().getText()
            column = ctx.STRING().getText().strip('"')
            
            # Validar existencia de columna
            if column not in self.filtered_data.columns:
                raise CSVProcessingError(f"Columna '{column}' no encontrada")
            
            # Validar tipo para operaciones numéricas
            if func in ['SUM', 'AVERAGE']:
                if not pd.api.types.is_numeric_dtype(self.filtered_data[column]):
                    raise CSVProcessingError(f"Columna '{column}' debe ser numérica")
            
            # Aplicar filtro WHERE si existe
            subset = self.filtered_data
            if ctx.expr():
                condition = self.visit(ctx.expr())
                subset = self.filtered_data[condition]
                print(f"🔧 Filtro WHERE aplicado. Registros usados: {len(subset)}")
            
            # Ejecutar agregación
            if func == "SUM":
                self.aggregation_result = subset[column].sum()
            elif func == "COUNT":
                self.aggregation_result = subset.shape[0]
            elif func == "AVERAGE":
                self.aggregation_result = subset[column].mean()
            else:
                raise CSVProcessingError(f"Función no soportada: {func}")
            
            print(f"\n📊 Resultado de {func}({column}): {self.aggregation_result:.2f}")
            
        except CSVProcessingError as e:
            print(f"❌ Error en agregación: {e}")

    def visitPrintStat(self, ctx):
        """Procesa el comando PRINT"""
        print("\n📄 Datos actuales:")
        print(self.filtered_data.to_string(index=False))
        print(f"\nMostrando {len(self.filtered_data)} de {len(self.original_data)} registros")

    def visitLogicalExpr(self, ctx):
        """Maneja expresiones lógicas (AND/OR)"""
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
        """Maneja comparaciones (=, !=, >, <, etc)"""
        try:
            col = ctx.STRING().getText().strip('"')
            operator = ctx.OPERATOR().getText()
            value = self.visit(ctx.value())
            
            # Validar columna
            if col not in self.original_data.columns:
                raise CSVProcessingError(f"Columna '{col}' no existe")
            
            # Validar tipo de datos
            col_type = self.original_data[col].dtype
            if isinstance(value, (int, float)) and not pd.api.types.is_numeric_dtype(col_type):
                raise CSVProcessingError(f"Columna '{col}' no es numérica")
            elif isinstance(value, str) and pd.api.types.is_numeric_dtype(col_type):
                raise CSVProcessingError(f"Columna '{col}' es numérica, no se puede comparar con texto")
            
            # Generar condición
            if operator == "==": return self.original_data[col] == value
            elif operator == "!=": return self.original_data[col] != value
            elif operator == ">": return self.original_data[col] > value
            elif operator == "<": return self.original_data[col] < value
            elif operator == ">=": return self.original_data[col] >= value
            elif operator == "<=": return self.original_data[col] <= value
            
        except Exception as e:
            print(f"❌ Error en condición: {str(e)}")
            return pd.Series(False, index=self.original_data.index)

    def visitBetweenExpr(self, ctx):
        try:
            col = ctx.STRING().getText().strip('"')
            lower = self.visit(ctx.value(0))  # ❌ Error: Paréntesis extra
            upper = self.visit(ctx.value(1))  # ❌ Error: Paréntesis extra
            
            # Validar columna
            if col not in self.original_data.columns:
                raise CSVProcessingError(f"Columna '{col}' no existe")
                
            # Convertir fechas
            if "fecha" in col:
                self.original_data[col] = pd.to_datetime(
                    self.original_data[col], 
                    errors='coerce'
                    )
            lower = pd.to_datetime(lower)
            upper = pd.to_datetime(upper)
            
            return self.original_data[col].between(lower, upper, inclusive='both')
            
        except Exception as e:
            print(f"❌ Error en BETWEEN: {str(e)}")
            return pd.Series(False, index=self.original_data.index)

    def visitValue(self, ctx):
        """Convierte valores a tipos Python apropiados"""
        if ctx.NUMBER():
            num_str = ctx.NUMBER().getText()
            return float(num_str) if '.' in num_str else int(num_str)
        elif ctx.STRING():
            return ctx.STRING().getText().strip('"')