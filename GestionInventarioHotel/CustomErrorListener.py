from antlr4.error.ErrorListener import ErrorListener # type: ignore

class CustomErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        print(f"Error en línea {line}, columna {column}: {msg}")