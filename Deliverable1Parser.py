# Generated from Deliverable1.g4 by ANTLR 4.13.2
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
        4,1,22,65,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,5,0,12,8,0,
        10,0,12,0,15,9,0,1,0,1,0,1,1,1,1,3,1,21,8,1,1,2,1,2,1,2,1,2,1,2,
        1,2,3,2,29,8,2,1,3,1,3,1,3,1,3,1,3,1,3,5,3,37,8,3,10,3,12,3,40,9,
        3,3,3,42,8,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,55,
        8,4,1,4,1,4,1,4,5,4,60,8,4,10,4,12,4,63,9,4,1,4,0,1,8,5,0,2,4,6,
        8,0,2,1,0,2,5,1,0,9,13,69,0,13,1,0,0,0,2,20,1,0,0,0,4,28,1,0,0,0,
        6,30,1,0,0,0,8,54,1,0,0,0,10,12,3,2,1,0,11,10,1,0,0,0,12,15,1,0,
        0,0,13,11,1,0,0,0,13,14,1,0,0,0,14,16,1,0,0,0,15,13,1,0,0,0,16,17,
        5,0,0,1,17,1,1,0,0,0,18,21,3,4,2,0,19,21,3,6,3,0,20,18,1,0,0,0,20,
        19,1,0,0,0,21,3,1,0,0,0,22,23,5,16,0,0,23,24,5,1,0,0,24,29,3,8,4,
        0,25,26,5,16,0,0,26,27,7,0,0,0,27,29,3,8,4,0,28,22,1,0,0,0,28,25,
        1,0,0,0,29,5,1,0,0,0,30,31,5,16,0,0,31,32,5,1,0,0,32,41,5,6,0,0,
        33,38,3,8,4,0,34,35,5,7,0,0,35,37,3,8,4,0,36,34,1,0,0,0,37,40,1,
        0,0,0,38,36,1,0,0,0,38,39,1,0,0,0,39,42,1,0,0,0,40,38,1,0,0,0,41,
        33,1,0,0,0,41,42,1,0,0,0,42,43,1,0,0,0,43,44,5,8,0,0,44,7,1,0,0,
        0,45,46,6,4,-1,0,46,55,5,16,0,0,47,55,5,17,0,0,48,55,5,18,0,0,49,
        55,5,19,0,0,50,51,5,14,0,0,51,52,3,8,4,0,52,53,5,15,0,0,53,55,1,
        0,0,0,54,45,1,0,0,0,54,47,1,0,0,0,54,48,1,0,0,0,54,49,1,0,0,0,54,
        50,1,0,0,0,55,61,1,0,0,0,56,57,10,6,0,0,57,58,7,1,0,0,58,60,3,8,
        4,7,59,56,1,0,0,0,60,63,1,0,0,0,61,59,1,0,0,0,61,62,1,0,0,0,62,9,
        1,0,0,0,63,61,1,0,0,0,7,13,20,28,38,41,54,61
    ]

class Deliverable1Parser ( Parser ):

    grammarFileName = "Deliverable1.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "'+='", "'-='", "'*='", "'/='", 
                     "'['", "','", "']'", "'+'", "'-'", "'*'", "'/'", "'%'", 
                     "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "VARNAME", "NUMBER", "BOOLEAN", "STRING", "WS", "TAB", 
                      "COMMENT" ]

    RULE_prog = 0
    RULE_s = 1
    RULE_assignment = 2
    RULE_array_assignment = 3
    RULE_expr = 4

    ruleNames =  [ "prog", "s", "assignment", "array_assignment", "expr" ]

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
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    VARNAME=16
    NUMBER=17
    BOOLEAN=18
    STRING=19
    WS=20
    TAB=21
    COMMENT=22

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

        def EOF(self):
            return self.getToken(Deliverable1Parser.EOF, 0)

        def s(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Deliverable1Parser.SContext)
            else:
                return self.getTypedRuleContext(Deliverable1Parser.SContext,i)


        def getRuleIndex(self):
            return Deliverable1Parser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)




    def prog(self):

        localctx = Deliverable1Parser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 13
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==16:
                self.state = 10
                self.s()
                self.state = 15
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 16
            self.match(Deliverable1Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment(self):
            return self.getTypedRuleContext(Deliverable1Parser.AssignmentContext,0)


        def array_assignment(self):
            return self.getTypedRuleContext(Deliverable1Parser.Array_assignmentContext,0)


        def getRuleIndex(self):
            return Deliverable1Parser.RULE_s

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterS" ):
                listener.enterS(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitS" ):
                listener.exitS(self)




    def s(self):

        localctx = Deliverable1Parser.SContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_s)
        try:
            self.state = 20
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 18
                self.assignment()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 19
                self.array_assignment()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARNAME(self):
            return self.getToken(Deliverable1Parser.VARNAME, 0)

        def expr(self):
            return self.getTypedRuleContext(Deliverable1Parser.ExprContext,0)


        def getRuleIndex(self):
            return Deliverable1Parser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)




    def assignment(self):

        localctx = Deliverable1Parser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_assignment)
        self._la = 0 # Token type
        try:
            self.state = 28
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 22
                self.match(Deliverable1Parser.VARNAME)
                self.state = 23
                self.match(Deliverable1Parser.T__0)
                self.state = 24
                self.expr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 25
                self.match(Deliverable1Parser.VARNAME)
                self.state = 26
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 60) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 27
                self.expr(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_assignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARNAME(self):
            return self.getToken(Deliverable1Parser.VARNAME, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Deliverable1Parser.ExprContext)
            else:
                return self.getTypedRuleContext(Deliverable1Parser.ExprContext,i)


        def getRuleIndex(self):
            return Deliverable1Parser.RULE_array_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArray_assignment" ):
                listener.enterArray_assignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArray_assignment" ):
                listener.exitArray_assignment(self)




    def array_assignment(self):

        localctx = Deliverable1Parser.Array_assignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_array_assignment)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self.match(Deliverable1Parser.VARNAME)
            self.state = 31
            self.match(Deliverable1Parser.T__0)
            self.state = 32
            self.match(Deliverable1Parser.T__5)
            self.state = 41
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 999424) != 0):
                self.state = 33
                self.expr(0)
                self.state = 38
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==7:
                    self.state = 34
                    self.match(Deliverable1Parser.T__6)
                    self.state = 35
                    self.expr(0)
                    self.state = 40
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 43
            self.match(Deliverable1Parser.T__7)
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

        def VARNAME(self):
            return self.getToken(Deliverable1Parser.VARNAME, 0)

        def NUMBER(self):
            return self.getToken(Deliverable1Parser.NUMBER, 0)

        def BOOLEAN(self):
            return self.getToken(Deliverable1Parser.BOOLEAN, 0)

        def STRING(self):
            return self.getToken(Deliverable1Parser.STRING, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Deliverable1Parser.ExprContext)
            else:
                return self.getTypedRuleContext(Deliverable1Parser.ExprContext,i)


        def getRuleIndex(self):
            return Deliverable1Parser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = Deliverable1Parser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 8
        self.enterRecursionRule(localctx, 8, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16]:
                self.state = 46
                self.match(Deliverable1Parser.VARNAME)
                pass
            elif token in [17]:
                self.state = 47
                self.match(Deliverable1Parser.NUMBER)
                pass
            elif token in [18]:
                self.state = 48
                self.match(Deliverable1Parser.BOOLEAN)
                pass
            elif token in [19]:
                self.state = 49
                self.match(Deliverable1Parser.STRING)
                pass
            elif token in [14]:
                self.state = 50
                self.match(Deliverable1Parser.T__13)
                self.state = 51
                self.expr(0)
                self.state = 52
                self.match(Deliverable1Parser.T__14)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 61
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = Deliverable1Parser.ExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 56
                    if not self.precpred(self._ctx, 6):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                    self.state = 57
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 15872) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 58
                    self.expr(7) 
                self.state = 63
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[4] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 6)
         




