# Generated from CSVFilter.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .CSVFilterParser import CSVFilterParser
else:
    from CSVFilterParser import CSVFilterParser

# This class defines a complete listener for a parse tree produced by CSVFilterParser.
class CSVFilterListener(ParseTreeListener):

    # Enter a parse tree produced by CSVFilterParser#prog.
    def enterProg(self, ctx:CSVFilterParser.ProgContext):
        pass

    # Exit a parse tree produced by CSVFilterParser#prog.
    def exitProg(self, ctx:CSVFilterParser.ProgContext):
        pass


    # Enter a parse tree produced by CSVFilterParser#stat.
    def enterStat(self, ctx:CSVFilterParser.StatContext):
        pass

    # Exit a parse tree produced by CSVFilterParser#stat.
    def exitStat(self, ctx:CSVFilterParser.StatContext):
        pass


    # Enter a parse tree produced by CSVFilterParser#loadStat.
    def enterLoadStat(self, ctx:CSVFilterParser.LoadStatContext):
        pass

    # Exit a parse tree produced by CSVFilterParser#loadStat.
    def exitLoadStat(self, ctx:CSVFilterParser.LoadStatContext):
        pass


    # Enter a parse tree produced by CSVFilterParser#filterStat.
    def enterFilterStat(self, ctx:CSVFilterParser.FilterStatContext):
        pass

    # Exit a parse tree produced by CSVFilterParser#filterStat.
    def exitFilterStat(self, ctx:CSVFilterParser.FilterStatContext):
        pass


    # Enter a parse tree produced by CSVFilterParser#aggregateStat.
    def enterAggregateStat(self, ctx:CSVFilterParser.AggregateStatContext):
        pass

    # Exit a parse tree produced by CSVFilterParser#aggregateStat.
    def exitAggregateStat(self, ctx:CSVFilterParser.AggregateStatContext):
        pass


    # Enter a parse tree produced by CSVFilterParser#printStat.
    def enterPrintStat(self, ctx:CSVFilterParser.PrintStatContext):
        pass

    # Exit a parse tree produced by CSVFilterParser#printStat.
    def exitPrintStat(self, ctx:CSVFilterParser.PrintStatContext):
        pass


    # Enter a parse tree produced by CSVFilterParser#logicalExpr.
    def enterLogicalExpr(self, ctx:CSVFilterParser.LogicalExprContext):
        pass

    # Exit a parse tree produced by CSVFilterParser#logicalExpr.
    def exitLogicalExpr(self, ctx:CSVFilterParser.LogicalExprContext):
        pass


    # Enter a parse tree produced by CSVFilterParser#comparisonExpr.
    def enterComparisonExpr(self, ctx:CSVFilterParser.ComparisonExprContext):
        pass

    # Exit a parse tree produced by CSVFilterParser#comparisonExpr.
    def exitComparisonExpr(self, ctx:CSVFilterParser.ComparisonExprContext):
        pass


    # Enter a parse tree produced by CSVFilterParser#betweenExpr.
    def enterBetweenExpr(self, ctx:CSVFilterParser.BetweenExprContext):
        pass

    # Exit a parse tree produced by CSVFilterParser#betweenExpr.
    def exitBetweenExpr(self, ctx:CSVFilterParser.BetweenExprContext):
        pass


    # Enter a parse tree produced by CSVFilterParser#value.
    def enterValue(self, ctx:CSVFilterParser.ValueContext):
        pass

    # Exit a parse tree produced by CSVFilterParser#value.
    def exitValue(self, ctx:CSVFilterParser.ValueContext):
        pass



del CSVFilterParser