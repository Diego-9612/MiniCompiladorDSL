# Generated from CSVFilter.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,15,72,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,1,0,4,0,18,8,0,11,0,12,0,19,1,1,1,1,1,1,1,1,3,1,26,8,1,
        1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,3,4,
        43,8,4,1,4,1,4,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,
        6,3,6,60,8,6,1,6,1,6,1,6,5,6,65,8,6,10,6,12,6,68,9,6,1,7,1,7,1,7,
        0,1,12,8,0,2,4,6,8,10,12,14,0,1,1,0,13,14,70,0,17,1,0,0,0,2,25,1,
        0,0,0,4,27,1,0,0,0,6,31,1,0,0,0,8,36,1,0,0,0,10,46,1,0,0,0,12,59,
        1,0,0,0,14,69,1,0,0,0,16,18,3,2,1,0,17,16,1,0,0,0,18,19,1,0,0,0,
        19,17,1,0,0,0,19,20,1,0,0,0,20,1,1,0,0,0,21,26,3,4,2,0,22,26,3,6,
        3,0,23,26,3,8,4,0,24,26,3,10,5,0,25,21,1,0,0,0,25,22,1,0,0,0,25,
        23,1,0,0,0,25,24,1,0,0,0,26,3,1,0,0,0,27,28,5,1,0,0,28,29,5,13,0,
        0,29,30,5,2,0,0,30,5,1,0,0,0,31,32,5,3,0,0,32,33,5,4,0,0,33,34,3,
        12,6,0,34,35,5,2,0,0,35,7,1,0,0,0,36,37,5,5,0,0,37,38,5,10,0,0,38,
        39,5,4,0,0,39,42,5,13,0,0,40,41,5,6,0,0,41,43,3,12,6,0,42,40,1,0,
        0,0,42,43,1,0,0,0,43,44,1,0,0,0,44,45,5,2,0,0,45,9,1,0,0,0,46,47,
        5,7,0,0,47,48,5,2,0,0,48,11,1,0,0,0,49,50,6,6,-1,0,50,51,5,13,0,
        0,51,52,5,12,0,0,52,60,3,14,7,0,53,54,5,13,0,0,54,55,5,8,0,0,55,
        56,3,14,7,0,56,57,5,9,0,0,57,58,3,14,7,0,58,60,1,0,0,0,59,49,1,0,
        0,0,59,53,1,0,0,0,60,66,1,0,0,0,61,62,10,3,0,0,62,63,5,11,0,0,63,
        65,3,12,6,4,64,61,1,0,0,0,65,68,1,0,0,0,66,64,1,0,0,0,66,67,1,0,
        0,0,67,13,1,0,0,0,68,66,1,0,0,0,69,70,7,0,0,0,70,15,1,0,0,0,5,19,
        25,42,59,66
    ]

class CSVFilterParser ( Parser ):

    grammarFileName = "CSVFilter.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'load'", "';'", "'filter'", "'column'", 
                     "'aggregate'", "'where'", "'print'", "'BETWEEN'", "'AND'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "FUNC_NAME", "LOGICAL_OP", 
                      "OPERATOR", "STRING", "NUMBER", "WS" ]

    RULE_prog = 0
    RULE_stat = 1
    RULE_loadStat = 2
    RULE_filterStat = 3
    RULE_aggregateStat = 4
    RULE_printStat = 5
    RULE_expr = 6
    RULE_value = 7

    ruleNames =  [ "prog", "stat", "loadStat", "filterStat", "aggregateStat", 
                   "printStat", "expr", "value" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    FUNC_NAME=10
    LOGICAL_OP=11
    OPERATOR=12
    STRING=13
    NUMBER=14
    WS=15

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSVFilterParser.StatContext)
            else:
                return self.getTypedRuleContext(CSVFilterParser.StatContext,i)


        def getRuleIndex(self):
            return CSVFilterParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = CSVFilterParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 17 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 16
                self.stat()
                self.state = 19 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 170) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def loadStat(self):
            return self.getTypedRuleContext(CSVFilterParser.LoadStatContext,0)


        def filterStat(self):
            return self.getTypedRuleContext(CSVFilterParser.FilterStatContext,0)


        def aggregateStat(self):
            return self.getTypedRuleContext(CSVFilterParser.AggregateStatContext,0)


        def printStat(self):
            return self.getTypedRuleContext(CSVFilterParser.PrintStatContext,0)


        def getRuleIndex(self):
            return CSVFilterParser.RULE_stat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStat" ):
                listener.enterStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStat" ):
                listener.exitStat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStat" ):
                return visitor.visitStat(self)
            else:
                return visitor.visitChildren(self)




    def stat(self):

        localctx = CSVFilterParser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stat)
        try:
            self.state = 25
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 21
                self.loadStat()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 22
                self.filterStat()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 3)
                self.state = 23
                self.aggregateStat()
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 4)
                self.state = 24
                self.printStat()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LoadStatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(CSVFilterParser.STRING, 0)

        def getRuleIndex(self):
            return CSVFilterParser.RULE_loadStat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLoadStat" ):
                listener.enterLoadStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLoadStat" ):
                listener.exitLoadStat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoadStat" ):
                return visitor.visitLoadStat(self)
            else:
                return visitor.visitChildren(self)




    def loadStat(self):

        localctx = CSVFilterParser.LoadStatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_loadStat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27
            self.match(CSVFilterParser.T__0)
            self.state = 28
            self.match(CSVFilterParser.STRING)
            self.state = 29
            self.match(CSVFilterParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FilterStatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(CSVFilterParser.ExprContext,0)


        def getRuleIndex(self):
            return CSVFilterParser.RULE_filterStat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFilterStat" ):
                listener.enterFilterStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFilterStat" ):
                listener.exitFilterStat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFilterStat" ):
                return visitor.visitFilterStat(self)
            else:
                return visitor.visitChildren(self)




    def filterStat(self):

        localctx = CSVFilterParser.FilterStatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_filterStat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31
            self.match(CSVFilterParser.T__2)
            self.state = 32
            self.match(CSVFilterParser.T__3)
            self.state = 33
            self.expr(0)
            self.state = 34
            self.match(CSVFilterParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AggregateStatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC_NAME(self):
            return self.getToken(CSVFilterParser.FUNC_NAME, 0)

        def STRING(self):
            return self.getToken(CSVFilterParser.STRING, 0)

        def expr(self):
            return self.getTypedRuleContext(CSVFilterParser.ExprContext,0)


        def getRuleIndex(self):
            return CSVFilterParser.RULE_aggregateStat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAggregateStat" ):
                listener.enterAggregateStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAggregateStat" ):
                listener.exitAggregateStat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAggregateStat" ):
                return visitor.visitAggregateStat(self)
            else:
                return visitor.visitChildren(self)




    def aggregateStat(self):

        localctx = CSVFilterParser.AggregateStatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_aggregateStat)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            self.match(CSVFilterParser.T__4)
            self.state = 37
            self.match(CSVFilterParser.FUNC_NAME)
            self.state = 38
            self.match(CSVFilterParser.T__3)
            self.state = 39
            self.match(CSVFilterParser.STRING)
            self.state = 42
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6:
                self.state = 40
                self.match(CSVFilterParser.T__5)
                self.state = 41
                self.expr(0)


            self.state = 44
            self.match(CSVFilterParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintStatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CSVFilterParser.RULE_printStat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintStat" ):
                listener.enterPrintStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintStat" ):
                listener.exitPrintStat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintStat" ):
                return visitor.visitPrintStat(self)
            else:
                return visitor.visitChildren(self)




    def printStat(self):

        localctx = CSVFilterParser.PrintStatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_printStat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self.match(CSVFilterParser.T__6)
            self.state = 47
            self.match(CSVFilterParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CSVFilterParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class LogicalExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CSVFilterParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSVFilterParser.ExprContext)
            else:
                return self.getTypedRuleContext(CSVFilterParser.ExprContext,i)

        def LOGICAL_OP(self):
            return self.getToken(CSVFilterParser.LOGICAL_OP, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicalExpr" ):
                listener.enterLogicalExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicalExpr" ):
                listener.exitLogicalExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicalExpr" ):
                return visitor.visitLogicalExpr(self)
            else:
                return visitor.visitChildren(self)


    class ComparisonExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CSVFilterParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(CSVFilterParser.STRING, 0)
        def OPERATOR(self):
            return self.getToken(CSVFilterParser.OPERATOR, 0)
        def value(self):
            return self.getTypedRuleContext(CSVFilterParser.ValueContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparisonExpr" ):
                listener.enterComparisonExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparisonExpr" ):
                listener.exitComparisonExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComparisonExpr" ):
                return visitor.visitComparisonExpr(self)
            else:
                return visitor.visitChildren(self)


    class BetweenExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CSVFilterParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(CSVFilterParser.STRING, 0)
        def value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSVFilterParser.ValueContext)
            else:
                return self.getTypedRuleContext(CSVFilterParser.ValueContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBetweenExpr" ):
                listener.enterBetweenExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBetweenExpr" ):
                listener.exitBetweenExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBetweenExpr" ):
                return visitor.visitBetweenExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CSVFilterParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 12
        self.enterRecursionRule(localctx, 12, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                localctx = CSVFilterParser.ComparisonExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 50
                self.match(CSVFilterParser.STRING)
                self.state = 51
                self.match(CSVFilterParser.OPERATOR)
                self.state = 52
                self.value()
                pass

            elif la_ == 2:
                localctx = CSVFilterParser.BetweenExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 53
                self.match(CSVFilterParser.STRING)
                self.state = 54
                self.match(CSVFilterParser.T__7)
                self.state = 55
                self.value()
                self.state = 56
                self.match(CSVFilterParser.T__8)
                self.state = 57
                self.value()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 66
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSVFilterParser.LogicalExprContext(self, CSVFilterParser.ExprContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 61
                    if not self.precpred(self._ctx, 3):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                    self.state = 62
                    self.match(CSVFilterParser.LOGICAL_OP)
                    self.state = 63
                    self.expr(4) 
                self.state = 68
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(CSVFilterParser.NUMBER, 0)

        def STRING(self):
            return self.getToken(CSVFilterParser.STRING, 0)

        def getRuleIndex(self):
            return CSVFilterParser.RULE_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue" ):
                listener.enterValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue" ):
                listener.exitValue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValue" ):
                return visitor.visitValue(self)
            else:
                return visitor.visitChildren(self)




    def value(self):

        localctx = CSVFilterParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_value)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            _la = self._input.LA(1)
            if not(_la==13 or _la==14):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[6] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         




