# Generated from CSVFilter.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .CSVFilterParser import CSVFilterParser
else:
    from CSVFilterParser import CSVFilterParser

# This class defines a complete generic visitor for a parse tree produced by CSVFilterParser.

class CSVFilterVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CSVFilterParser#prog.
    def visitProg(self, ctx:CSVFilterParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSVFilterParser#stat.
    def visitStat(self, ctx:CSVFilterParser.StatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSVFilterParser#loadStat.
    def visitLoadStat(self, ctx:CSVFilterParser.LoadStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSVFilterParser#filterStat.
    def visitFilterStat(self, ctx:CSVFilterParser.FilterStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSVFilterParser#aggregateStat.
    def visitAggregateStat(self, ctx:CSVFilterParser.AggregateStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSVFilterParser#printStat.
    def visitPrintStat(self, ctx:CSVFilterParser.PrintStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSVFilterParser#logicalExpr.
    def visitLogicalExpr(self, ctx:CSVFilterParser.LogicalExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSVFilterParser#comparisonExpr.
    def visitComparisonExpr(self, ctx:CSVFilterParser.ComparisonExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSVFilterParser#betweenExpr.
    def visitBetweenExpr(self, ctx:CSVFilterParser.BetweenExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSVFilterParser#value.
    def visitValue(self, ctx:CSVFilterParser.ValueContext):
        return self.visitChildren(ctx)



del CSVFilterParser