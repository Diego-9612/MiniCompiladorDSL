from antlr4.error.ErrorListener import ErrorListener

class CustomErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        error_msg = f"🚨 Error de sintaxis línea {line}:{column} - {msg}"
        raise Exception(error_msg)
    
    def reportAmbiguity(self, recognizer, dfa, startIndex, stopIndex, exact, ambigAlts, configs):
        pass
    
    def reportAttemptingFullContext(self, recognizer, dfa, startIndex, stopIndex, conflictingAlts, configs):
        pass
    
    def reportContextSensitivity(self, recognizer, dfa, startIndex, stopIndex, prediction, configs):
        pass