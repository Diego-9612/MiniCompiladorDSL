import csv
from CSVFilterVisitor import CSVFilterVisitor

class MyCSVVisitor(CSVFilterVisitor):
    def __init__(self):
        self.data = []
        self.filtered_data = []
        self.filename = ""
        self.filtros = []

    def visitLoadStat(self, ctx):
        self.filename = ctx.STRING().getText().replace('"', '')
        with open(self.filename, newline='') as f:
            self.data = list(csv.DictReader(f))
        self.filtered_data = self.data
        return None

    def visitFilterStat(self, ctx):
        # Aquí manejamos los filtros compuestos, AND, OR, y BETWEEN
        expr = self.visit(ctx.expr())  # Se procesa la expresión que puede ser lógica o de comparación
        self.filtered_data = [
            row for row in self.filtered_data if expr(row)
        ]
        return None

    def visitAggregateStat(self, ctx):
        func = ctx.FUNC_NAME().getText()
        column = ctx.STRING().getText().replace('"', '')
        condition = ctx.expr()  # 'where' expresión condicional (opcional)

        if condition:
            condition_func = self.visit(condition)  # Filtramos si hay condición
            filtered_data = [row for row in self.data if condition_func(row)]
        else:
            filtered_data = self.data

        # Aplicar función de agregación
        if func == 'COUNT':
            print(f"Total registros en {column}: {len(filtered_data)}")
        elif func == 'SUM':
            total_sum = sum(int(row[column]) for row in filtered_data if row[column].isdigit())
            print(f"Suma de {column}: {total_sum}")
        elif func == 'AVERAGE':
            total_sum = sum(int(row[column]) for row in filtered_data if row[column].isdigit())
            average = total_sum / len(filtered_data) if len(filtered_data) > 0 else 0
            print(f"Promedio de {column}: {average:.2f}")

        return None

    def visitPrintStat(self, ctx):
        for row in self.filtered_data:
            print(row)
        return None

    def visitLogicalExpr(self, ctx):
        # Maneja las expresiones lógicas AND/OR
        left_expr = self.visit(ctx.expr(0))
        right_expr = self.visit(ctx.expr(1))
        logical_op = ctx.LOGICAL_OP().getText()

        if logical_op == "AND":
            return lambda row: left_expr(row) and right_expr(row)
        elif logical_op == "OR":
            return lambda row: left_expr(row) or right_expr(row)

    def visitComparisonExpr(self, ctx):
        column = ctx.STRING().getText().replace('"', '')
        op = ctx.OPERATOR().getText()
        value = ctx.value().getText().replace('"', '')  # Obtener el valor como texto (sin las comillas)

        # Verificar si el valor es numérico o una cadena
        try:
            # Intentar convertir el valor a un número (float o int)
            value = float(value)
            is_numeric = True
        except ValueError:
            # Si no se puede convertir a número, es una cadena
            is_numeric = False

        # Si es numérico, realizamos la comparación numérica
        if is_numeric:
            return lambda row: eval(f"{float(row[column])} {op} {value}")
        else:
            # Si es cadena, realizamos la comparación de cadenas
            return lambda row: eval(f"'{row[column]}' {op} '{value}'")

    def visitBetweenExpr(self, ctx):
        column = ctx.STRING().getText().replace('"', '')
        low_value = float(ctx.value(0).getText())
        high_value = float(ctx.value(1).getText())

        # Expresión de tipo BETWEEN
        return lambda row: low_value <= float(row[column]) <= high_value

