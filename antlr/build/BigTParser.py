# Generated from BigT.g4 by ANTLR 4.13.1
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
        4,1,29,176,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,1,0,1,0,1,0,1,1,1,1,1,1,
        1,1,1,1,1,1,3,1,46,8,1,1,2,1,2,1,2,1,3,1,3,1,3,1,4,1,4,3,4,56,8,
        4,1,5,1,5,3,5,60,8,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,
        1,6,1,6,1,6,3,6,76,8,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,
        7,1,7,1,7,1,7,3,7,92,8,7,1,8,1,8,3,8,96,8,8,1,9,1,9,1,9,1,9,1,10,
        1,10,1,10,1,11,1,11,1,11,3,11,108,8,11,1,11,1,11,1,11,3,11,113,8,
        11,1,11,1,11,1,11,3,11,118,8,11,1,11,1,11,1,11,3,11,123,8,11,1,11,
        1,11,1,11,3,11,128,8,11,3,11,130,8,11,1,12,1,12,1,12,1,13,1,13,1,
        13,3,13,138,8,13,1,13,1,13,1,13,3,13,143,8,13,3,13,145,8,13,1,14,
        1,14,3,14,149,8,14,1,15,1,15,1,15,3,15,154,8,15,1,15,1,15,1,15,3,
        15,159,8,15,3,15,161,8,15,1,16,1,16,1,16,1,16,1,16,1,16,3,16,169,
        8,16,1,17,1,17,1,17,1,17,1,17,1,17,0,0,18,0,2,4,6,8,10,12,14,16,
        18,20,22,24,26,28,30,32,34,0,0,181,0,36,1,0,0,0,2,45,1,0,0,0,4,47,
        1,0,0,0,6,50,1,0,0,0,8,55,1,0,0,0,10,59,1,0,0,0,12,75,1,0,0,0,14,
        91,1,0,0,0,16,95,1,0,0,0,18,97,1,0,0,0,20,101,1,0,0,0,22,129,1,0,
        0,0,24,131,1,0,0,0,26,144,1,0,0,0,28,146,1,0,0,0,30,160,1,0,0,0,
        32,168,1,0,0,0,34,170,1,0,0,0,36,37,3,2,1,0,37,38,5,25,0,0,38,1,
        1,0,0,0,39,40,3,4,2,0,40,41,5,25,0,0,41,46,1,0,0,0,42,43,3,6,3,0,
        43,44,5,25,0,0,44,46,1,0,0,0,45,39,1,0,0,0,45,42,1,0,0,0,46,3,1,
        0,0,0,47,48,5,26,0,0,48,49,3,8,4,0,49,5,1,0,0,0,50,51,5,27,0,0,51,
        52,3,8,4,0,52,7,1,0,0,0,53,56,3,18,9,0,54,56,3,10,5,0,55,53,1,0,
        0,0,55,54,1,0,0,0,56,9,1,0,0,0,57,60,3,12,6,0,58,60,3,14,7,0,59,
        57,1,0,0,0,59,58,1,0,0,0,60,11,1,0,0,0,61,62,5,4,0,0,62,63,5,1,0,
        0,63,64,3,20,10,0,64,65,5,2,0,0,65,66,3,12,6,0,66,67,5,5,0,0,67,
        68,3,12,6,0,68,76,1,0,0,0,69,70,5,6,0,0,70,71,5,1,0,0,71,72,3,20,
        10,0,72,73,5,2,0,0,73,74,3,10,5,0,74,76,1,0,0,0,75,61,1,0,0,0,75,
        69,1,0,0,0,76,13,1,0,0,0,77,78,5,4,0,0,78,79,5,1,0,0,79,80,3,20,
        10,0,80,81,5,2,0,0,81,82,3,10,5,0,82,92,1,0,0,0,83,84,5,4,0,0,84,
        85,5,1,0,0,85,86,3,20,10,0,86,87,5,2,0,0,87,88,3,12,6,0,88,89,5,
        5,0,0,89,90,3,14,7,0,90,92,1,0,0,0,91,77,1,0,0,0,91,83,1,0,0,0,92,
        15,1,0,0,0,93,96,5,28,0,0,94,96,5,19,0,0,95,93,1,0,0,0,95,94,1,0,
        0,0,96,17,1,0,0,0,97,98,5,20,0,0,98,99,5,3,0,0,99,100,3,24,12,0,
        100,19,1,0,0,0,101,102,3,28,14,0,102,103,3,22,11,0,103,21,1,0,0,
        0,104,105,5,10,0,0,105,107,3,28,14,0,106,108,3,22,11,0,107,106,1,
        0,0,0,107,108,1,0,0,0,108,130,1,0,0,0,109,110,5,11,0,0,110,112,3,
        28,14,0,111,113,3,22,11,0,112,111,1,0,0,0,112,113,1,0,0,0,113,130,
        1,0,0,0,114,115,5,12,0,0,115,117,3,28,14,0,116,118,3,22,11,0,117,
        116,1,0,0,0,117,118,1,0,0,0,118,130,1,0,0,0,119,120,5,13,0,0,120,
        122,3,28,14,0,121,123,3,22,11,0,122,121,1,0,0,0,122,123,1,0,0,0,
        123,130,1,0,0,0,124,125,5,14,0,0,125,127,3,28,14,0,126,128,3,22,
        11,0,127,126,1,0,0,0,127,128,1,0,0,0,128,130,1,0,0,0,129,104,1,0,
        0,0,129,109,1,0,0,0,129,114,1,0,0,0,129,119,1,0,0,0,129,124,1,0,
        0,0,130,23,1,0,0,0,131,132,3,28,14,0,132,133,3,26,13,0,133,25,1,
        0,0,0,134,135,5,17,0,0,135,137,3,28,14,0,136,138,3,26,13,0,137,136,
        1,0,0,0,137,138,1,0,0,0,138,145,1,0,0,0,139,140,5,18,0,0,140,142,
        3,28,14,0,141,143,3,26,13,0,142,141,1,0,0,0,142,143,1,0,0,0,143,
        145,1,0,0,0,144,134,1,0,0,0,144,139,1,0,0,0,145,27,1,0,0,0,146,148,
        3,32,16,0,147,149,3,30,15,0,148,147,1,0,0,0,148,149,1,0,0,0,149,
        29,1,0,0,0,150,151,5,15,0,0,151,153,3,32,16,0,152,154,3,30,15,0,
        153,152,1,0,0,0,153,154,1,0,0,0,154,161,1,0,0,0,155,156,5,16,0,0,
        156,158,3,32,16,0,157,159,3,30,15,0,158,157,1,0,0,0,158,159,1,0,
        0,0,159,161,1,0,0,0,160,150,1,0,0,0,160,155,1,0,0,0,161,31,1,0,0,
        0,162,169,5,21,0,0,163,169,5,20,0,0,164,165,5,1,0,0,165,166,3,24,
        12,0,166,167,5,2,0,0,167,169,1,0,0,0,168,162,1,0,0,0,168,163,1,0,
        0,0,168,164,1,0,0,0,169,33,1,0,0,0,170,171,5,22,0,0,171,172,5,20,
        0,0,172,173,5,23,0,0,173,174,5,24,0,0,174,35,1,0,0,0,20,45,55,59,
        75,91,95,107,112,117,122,127,129,137,142,144,148,153,158,160,168
    ]

class BigTParser ( Parser ):

    grammarFileName = "BigT.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'='", "'IF'", "'ELSE'", 
                     "'WHILE'", "'&&'", "'||'", "'!'", "'>='", "'<='", "'=='", 
                     "'<'", "'>'", "'*'", "'/'", "'+'", "'-'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'SEQ'", "'PAR'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "IF", "ELSE", "WHILE", "AND", "OR", "NOT", "GE", "LE", 
                      "EQ", "LT", "GT", "MUL", "DIV", "ADD", "SUB", "CHAR", 
                      "ID", "DIGIT", "CHAN", "ID_COMP1", "ID_COMP2", "NEWLINE", 
                      "SEQ", "PAR", "INT", "WS" ]

    RULE_progama_minipar = 0
    RULE_bloco_stmt = 1
    RULE_bloco_seq = 2
    RULE_bloco_par = 3
    RULE_stmts = 4
    RULE_stmt = 5
    RULE_cmd_a = 6
    RULE_cmd_na = 7
    RULE_tipos_var = 8
    RULE_atribuicao = 9
    RULE_bool = 10
    RULE_mais_bool = 11
    RULE_expr = 12
    RULE_mais_expr = 13
    RULE_termo = 14
    RULE_mais_termo = 15
    RULE_fator = 16
    RULE_c_chanel = 17

    ruleNames =  [ "progama_minipar", "bloco_stmt", "bloco_seq", "bloco_par", 
                   "stmts", "stmt", "cmd_a", "cmd_na", "tipos_var", "atribuicao", 
                   "bool", "mais_bool", "expr", "mais_expr", "termo", "mais_termo", 
                   "fator", "c_chanel" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    IF=4
    ELSE=5
    WHILE=6
    AND=7
    OR=8
    NOT=9
    GE=10
    LE=11
    EQ=12
    LT=13
    GT=14
    MUL=15
    DIV=16
    ADD=17
    SUB=18
    CHAR=19
    ID=20
    DIGIT=21
    CHAN=22
    ID_COMP1=23
    ID_COMP2=24
    NEWLINE=25
    SEQ=26
    PAR=27
    INT=28
    WS=29

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class Progama_miniparContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def bloco_stmt(self):
            return self.getTypedRuleContext(BigTParser.Bloco_stmtContext,0)


        def NEWLINE(self):
            return self.getToken(BigTParser.NEWLINE, 0)

        def getRuleIndex(self):
            return BigTParser.RULE_progama_minipar

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgama_minipar" ):
                listener.enterProgama_minipar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgama_minipar" ):
                listener.exitProgama_minipar(self)




    def progama_minipar(self):

        localctx = BigTParser.Progama_miniparContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_progama_minipar)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            self.bloco_stmt()
            self.state = 37
            self.match(BigTParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Bloco_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def bloco_seq(self):
            return self.getTypedRuleContext(BigTParser.Bloco_seqContext,0)


        def NEWLINE(self):
            return self.getToken(BigTParser.NEWLINE, 0)

        def bloco_par(self):
            return self.getTypedRuleContext(BigTParser.Bloco_parContext,0)


        def getRuleIndex(self):
            return BigTParser.RULE_bloco_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBloco_stmt" ):
                listener.enterBloco_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBloco_stmt" ):
                listener.exitBloco_stmt(self)




    def bloco_stmt(self):

        localctx = BigTParser.Bloco_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_bloco_stmt)
        try:
            self.state = 45
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [26]:
                self.enterOuterAlt(localctx, 1)
                self.state = 39
                self.bloco_seq()
                self.state = 40
                self.match(BigTParser.NEWLINE)
                pass
            elif token in [27]:
                self.enterOuterAlt(localctx, 2)
                self.state = 42
                self.bloco_par()
                self.state = 43
                self.match(BigTParser.NEWLINE)
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


    class Bloco_seqContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEQ(self):
            return self.getToken(BigTParser.SEQ, 0)

        def stmts(self):
            return self.getTypedRuleContext(BigTParser.StmtsContext,0)


        def getRuleIndex(self):
            return BigTParser.RULE_bloco_seq

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBloco_seq" ):
                listener.enterBloco_seq(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBloco_seq" ):
                listener.exitBloco_seq(self)




    def bloco_seq(self):

        localctx = BigTParser.Bloco_seqContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_bloco_seq)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self.match(BigTParser.SEQ)
            self.state = 48
            self.stmts()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Bloco_parContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PAR(self):
            return self.getToken(BigTParser.PAR, 0)

        def stmts(self):
            return self.getTypedRuleContext(BigTParser.StmtsContext,0)


        def getRuleIndex(self):
            return BigTParser.RULE_bloco_par

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBloco_par" ):
                listener.enterBloco_par(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBloco_par" ):
                listener.exitBloco_par(self)




    def bloco_par(self):

        localctx = BigTParser.Bloco_parContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_bloco_par)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self.match(BigTParser.PAR)
            self.state = 51
            self.stmts()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atribuicao(self):
            return self.getTypedRuleContext(BigTParser.AtribuicaoContext,0)


        def stmt(self):
            return self.getTypedRuleContext(BigTParser.StmtContext,0)


        def getRuleIndex(self):
            return BigTParser.RULE_stmts

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStmts" ):
                listener.enterStmts(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStmts" ):
                listener.exitStmts(self)




    def stmts(self):

        localctx = BigTParser.StmtsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_stmts)
        try:
            self.state = 55
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [20]:
                self.enterOuterAlt(localctx, 1)
                self.state = 53
                self.atribuicao()
                pass
            elif token in [4, 6]:
                self.enterOuterAlt(localctx, 2)
                self.state = 54
                self.stmt()
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


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def cmd_a(self):
            return self.getTypedRuleContext(BigTParser.Cmd_aContext,0)


        def cmd_na(self):
            return self.getTypedRuleContext(BigTParser.Cmd_naContext,0)


        def getRuleIndex(self):
            return BigTParser.RULE_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStmt" ):
                listener.enterStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStmt" ):
                listener.exitStmt(self)




    def stmt(self):

        localctx = BigTParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_stmt)
        try:
            self.state = 59
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 57
                self.cmd_a()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 58
                self.cmd_na()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Cmd_aContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return BigTParser.RULE_cmd_a

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class WHILEContext(Cmd_aContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BigTParser.Cmd_aContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def WHILE(self):
            return self.getToken(BigTParser.WHILE, 0)
        def bool_(self):
            return self.getTypedRuleContext(BigTParser.BoolContext,0)

        def stmt(self):
            return self.getTypedRuleContext(BigTParser.StmtContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWHILE" ):
                listener.enterWHILE(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWHILE" ):
                listener.exitWHILE(self)


    class IFelseContext(Cmd_aContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BigTParser.Cmd_aContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IF(self):
            return self.getToken(BigTParser.IF, 0)
        def bool_(self):
            return self.getTypedRuleContext(BigTParser.BoolContext,0)

        def cmd_a(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BigTParser.Cmd_aContext)
            else:
                return self.getTypedRuleContext(BigTParser.Cmd_aContext,i)

        def ELSE(self):
            return self.getToken(BigTParser.ELSE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIFelse" ):
                listener.enterIFelse(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIFelse" ):
                listener.exitIFelse(self)



    def cmd_a(self):

        localctx = BigTParser.Cmd_aContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_cmd_a)
        try:
            self.state = 75
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4]:
                localctx = BigTParser.IFelseContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 61
                self.match(BigTParser.IF)
                self.state = 62
                self.match(BigTParser.T__0)
                self.state = 63
                self.bool_()
                self.state = 64
                self.match(BigTParser.T__1)
                self.state = 65
                self.cmd_a()
                self.state = 66
                self.match(BigTParser.ELSE)
                self.state = 67
                self.cmd_a()
                pass
            elif token in [6]:
                localctx = BigTParser.WHILEContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 69
                self.match(BigTParser.WHILE)
                self.state = 70
                self.match(BigTParser.T__0)
                self.state = 71
                self.bool_()
                self.state = 72
                self.match(BigTParser.T__1)
                self.state = 73
                self.stmt()
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


    class Cmd_naContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return BigTParser.RULE_cmd_na

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class IFelsenaContext(Cmd_naContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BigTParser.Cmd_naContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IF(self):
            return self.getToken(BigTParser.IF, 0)
        def bool_(self):
            return self.getTypedRuleContext(BigTParser.BoolContext,0)

        def cmd_a(self):
            return self.getTypedRuleContext(BigTParser.Cmd_aContext,0)

        def ELSE(self):
            return self.getToken(BigTParser.ELSE, 0)
        def cmd_na(self):
            return self.getTypedRuleContext(BigTParser.Cmd_naContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIFelsena" ):
                listener.enterIFelsena(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIFelsena" ):
                listener.exitIFelsena(self)


    class IFContext(Cmd_naContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BigTParser.Cmd_naContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IF(self):
            return self.getToken(BigTParser.IF, 0)
        def bool_(self):
            return self.getTypedRuleContext(BigTParser.BoolContext,0)

        def stmt(self):
            return self.getTypedRuleContext(BigTParser.StmtContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIF" ):
                listener.enterIF(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIF" ):
                listener.exitIF(self)



    def cmd_na(self):

        localctx = BigTParser.Cmd_naContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_cmd_na)
        try:
            self.state = 91
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                localctx = BigTParser.IFContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 77
                self.match(BigTParser.IF)
                self.state = 78
                self.match(BigTParser.T__0)
                self.state = 79
                self.bool_()
                self.state = 80
                self.match(BigTParser.T__1)
                self.state = 81
                self.stmt()
                pass

            elif la_ == 2:
                localctx = BigTParser.IFelsenaContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 83
                self.match(BigTParser.IF)
                self.state = 84
                self.match(BigTParser.T__0)
                self.state = 85
                self.bool_()
                self.state = 86
                self.match(BigTParser.T__1)
                self.state = 87
                self.cmd_a()
                self.state = 88
                self.match(BigTParser.ELSE)
                self.state = 89
                self.cmd_na()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Tipos_varContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return BigTParser.RULE_tipos_var

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class CHARContext(Tipos_varContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BigTParser.Tipos_varContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def CHAR(self):
            return self.getToken(BigTParser.CHAR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCHAR" ):
                listener.enterCHAR(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCHAR" ):
                listener.exitCHAR(self)


    class INTContext(Tipos_varContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BigTParser.Tipos_varContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(BigTParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterINT" ):
                listener.enterINT(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitINT" ):
                listener.exitINT(self)



    def tipos_var(self):

        localctx = BigTParser.Tipos_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_tipos_var)
        try:
            self.state = 95
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [28]:
                localctx = BigTParser.INTContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 93
                self.match(BigTParser.INT)
                pass
            elif token in [19]:
                localctx = BigTParser.CHARContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 94
                self.match(BigTParser.CHAR)
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


    class AtribuicaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BigTParser.ID, 0)

        def expr(self):
            return self.getTypedRuleContext(BigTParser.ExprContext,0)


        def getRuleIndex(self):
            return BigTParser.RULE_atribuicao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtribuicao" ):
                listener.enterAtribuicao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtribuicao" ):
                listener.exitAtribuicao(self)




    def atribuicao(self):

        localctx = BigTParser.AtribuicaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_atribuicao)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            self.match(BigTParser.ID)
            self.state = 98
            self.match(BigTParser.T__2)
            self.state = 99
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BoolContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def termo(self):
            return self.getTypedRuleContext(BigTParser.TermoContext,0)


        def mais_bool(self):
            return self.getTypedRuleContext(BigTParser.Mais_boolContext,0)


        def getRuleIndex(self):
            return BigTParser.RULE_bool

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBool" ):
                listener.enterBool(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBool" ):
                listener.exitBool(self)




    def bool_(self):

        localctx = BigTParser.BoolContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_bool)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 101
            self.termo()
            self.state = 102
            self.mais_bool()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Mais_boolContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return BigTParser.RULE_mais_bool

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class LTContext(Mais_boolContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BigTParser.Mais_boolContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LT(self):
            return self.getToken(BigTParser.LT, 0)
        def termo(self):
            return self.getTypedRuleContext(BigTParser.TermoContext,0)

        def mais_bool(self):
            return self.getTypedRuleContext(BigTParser.Mais_boolContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLT" ):
                listener.enterLT(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLT" ):
                listener.exitLT(self)


    class LEContext(Mais_boolContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BigTParser.Mais_boolContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LE(self):
            return self.getToken(BigTParser.LE, 0)
        def termo(self):
            return self.getTypedRuleContext(BigTParser.TermoContext,0)

        def mais_bool(self):
            return self.getTypedRuleContext(BigTParser.Mais_boolContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLE" ):
                listener.enterLE(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLE" ):
                listener.exitLE(self)


    class EQContext(Mais_boolContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BigTParser.Mais_boolContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def EQ(self):
            return self.getToken(BigTParser.EQ, 0)
        def termo(self):
            return self.getTypedRuleContext(BigTParser.TermoContext,0)

        def mais_bool(self):
            return self.getTypedRuleContext(BigTParser.Mais_boolContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEQ" ):
                listener.enterEQ(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEQ" ):
                listener.exitEQ(self)


    class GTContext(Mais_boolContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BigTParser.Mais_boolContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def GT(self):
            return self.getToken(BigTParser.GT, 0)
        def termo(self):
            return self.getTypedRuleContext(BigTParser.TermoContext,0)

        def mais_bool(self):
            return self.getTypedRuleContext(BigTParser.Mais_boolContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGT" ):
                listener.enterGT(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGT" ):
                listener.exitGT(self)


    class GEContext(Mais_boolContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BigTParser.Mais_boolContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def GE(self):
            return self.getToken(BigTParser.GE, 0)
        def termo(self):
            return self.getTypedRuleContext(BigTParser.TermoContext,0)

        def mais_bool(self):
            return self.getTypedRuleContext(BigTParser.Mais_boolContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGE" ):
                listener.enterGE(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGE" ):
                listener.exitGE(self)



    def mais_bool(self):

        localctx = BigTParser.Mais_boolContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_mais_bool)
        self._la = 0 # Token type
        try:
            self.state = 129
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                localctx = BigTParser.GEContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 104
                self.match(BigTParser.GE)
                self.state = 105
                self.termo()
                self.state = 107
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 31744) != 0):
                    self.state = 106
                    self.mais_bool()


                pass
            elif token in [11]:
                localctx = BigTParser.LEContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 109
                self.match(BigTParser.LE)
                self.state = 110
                self.termo()
                self.state = 112
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 31744) != 0):
                    self.state = 111
                    self.mais_bool()


                pass
            elif token in [12]:
                localctx = BigTParser.EQContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 114
                self.match(BigTParser.EQ)
                self.state = 115
                self.termo()
                self.state = 117
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 31744) != 0):
                    self.state = 116
                    self.mais_bool()


                pass
            elif token in [13]:
                localctx = BigTParser.LTContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 119
                self.match(BigTParser.LT)
                self.state = 120
                self.termo()
                self.state = 122
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 31744) != 0):
                    self.state = 121
                    self.mais_bool()


                pass
            elif token in [14]:
                localctx = BigTParser.GTContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 124
                self.match(BigTParser.GT)
                self.state = 125
                self.termo()
                self.state = 127
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 31744) != 0):
                    self.state = 126
                    self.mais_bool()


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


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def termo(self):
            return self.getTypedRuleContext(BigTParser.TermoContext,0)


        def mais_expr(self):
            return self.getTypedRuleContext(BigTParser.Mais_exprContext,0)


        def getRuleIndex(self):
            return BigTParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)




    def expr(self):

        localctx = BigTParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 131
            self.termo()
            self.state = 132
            self.mais_expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Mais_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return BigTParser.RULE_mais_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ADDContext(Mais_exprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BigTParser.Mais_exprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ADD(self):
            return self.getToken(BigTParser.ADD, 0)
        def termo(self):
            return self.getTypedRuleContext(BigTParser.TermoContext,0)

        def mais_expr(self):
            return self.getTypedRuleContext(BigTParser.Mais_exprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterADD" ):
                listener.enterADD(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitADD" ):
                listener.exitADD(self)


    class SUBContext(Mais_exprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BigTParser.Mais_exprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def SUB(self):
            return self.getToken(BigTParser.SUB, 0)
        def termo(self):
            return self.getTypedRuleContext(BigTParser.TermoContext,0)

        def mais_expr(self):
            return self.getTypedRuleContext(BigTParser.Mais_exprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSUB" ):
                listener.enterSUB(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSUB" ):
                listener.exitSUB(self)



    def mais_expr(self):

        localctx = BigTParser.Mais_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_mais_expr)
        self._la = 0 # Token type
        try:
            self.state = 144
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [17]:
                localctx = BigTParser.ADDContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 134
                self.match(BigTParser.ADD)
                self.state = 135
                self.termo()
                self.state = 137
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==17 or _la==18:
                    self.state = 136
                    self.mais_expr()


                pass
            elif token in [18]:
                localctx = BigTParser.SUBContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 139
                self.match(BigTParser.SUB)
                self.state = 140
                self.termo()
                self.state = 142
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==17 or _la==18:
                    self.state = 141
                    self.mais_expr()


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


    class TermoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def fator(self):
            return self.getTypedRuleContext(BigTParser.FatorContext,0)


        def mais_termo(self):
            return self.getTypedRuleContext(BigTParser.Mais_termoContext,0)


        def getRuleIndex(self):
            return BigTParser.RULE_termo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTermo" ):
                listener.enterTermo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTermo" ):
                listener.exitTermo(self)




    def termo(self):

        localctx = BigTParser.TermoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_termo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 146
            self.fator()
            self.state = 148
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==15 or _la==16:
                self.state = 147
                self.mais_termo()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Mais_termoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return BigTParser.RULE_mais_termo

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class DIVContext(Mais_termoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BigTParser.Mais_termoContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def DIV(self):
            return self.getToken(BigTParser.DIV, 0)
        def fator(self):
            return self.getTypedRuleContext(BigTParser.FatorContext,0)

        def mais_termo(self):
            return self.getTypedRuleContext(BigTParser.Mais_termoContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDIV" ):
                listener.enterDIV(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDIV" ):
                listener.exitDIV(self)


    class MULContext(Mais_termoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BigTParser.Mais_termoContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def MUL(self):
            return self.getToken(BigTParser.MUL, 0)
        def fator(self):
            return self.getTypedRuleContext(BigTParser.FatorContext,0)

        def mais_termo(self):
            return self.getTypedRuleContext(BigTParser.Mais_termoContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMUL" ):
                listener.enterMUL(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMUL" ):
                listener.exitMUL(self)



    def mais_termo(self):

        localctx = BigTParser.Mais_termoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_mais_termo)
        self._la = 0 # Token type
        try:
            self.state = 160
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [15]:
                localctx = BigTParser.MULContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 150
                self.match(BigTParser.MUL)
                self.state = 151
                self.fator()
                self.state = 153
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==15 or _la==16:
                    self.state = 152
                    self.mais_termo()


                pass
            elif token in [16]:
                localctx = BigTParser.DIVContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 155
                self.match(BigTParser.DIV)
                self.state = 156
                self.fator()
                self.state = 158
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==15 or _la==16:
                    self.state = 157
                    self.mais_termo()


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


    class FatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return BigTParser.RULE_fator

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ParenexprParenContext(FatorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BigTParser.FatorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(BigTParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParenexprParen" ):
                listener.enterParenexprParen(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParenexprParen" ):
                listener.exitParenexprParen(self)


    class IDContext(FatorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BigTParser.FatorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(BigTParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterID" ):
                listener.enterID(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitID" ):
                listener.exitID(self)


    class DIGITContext(FatorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BigTParser.FatorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def DIGIT(self):
            return self.getToken(BigTParser.DIGIT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDIGIT" ):
                listener.enterDIGIT(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDIGIT" ):
                listener.exitDIGIT(self)



    def fator(self):

        localctx = BigTParser.FatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_fator)
        try:
            self.state = 168
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [21]:
                localctx = BigTParser.DIGITContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 162
                self.match(BigTParser.DIGIT)
                pass
            elif token in [20]:
                localctx = BigTParser.IDContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 163
                self.match(BigTParser.ID)
                pass
            elif token in [1]:
                localctx = BigTParser.ParenexprParenContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 164
                self.match(BigTParser.T__0)
                self.state = 165
                self.expr()
                self.state = 166
                self.match(BigTParser.T__1)
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


    class C_chanelContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CHAN(self):
            return self.getToken(BigTParser.CHAN, 0)

        def ID(self):
            return self.getToken(BigTParser.ID, 0)

        def ID_COMP1(self):
            return self.getToken(BigTParser.ID_COMP1, 0)

        def ID_COMP2(self):
            return self.getToken(BigTParser.ID_COMP2, 0)

        def getRuleIndex(self):
            return BigTParser.RULE_c_chanel

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterC_chanel" ):
                listener.enterC_chanel(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitC_chanel" ):
                listener.exitC_chanel(self)




    def c_chanel(self):

        localctx = BigTParser.C_chanelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_c_chanel)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 170
            self.match(BigTParser.CHAN)
            self.state = 171
            self.match(BigTParser.ID)
            self.state = 172
            self.match(BigTParser.ID_COMP1)
            self.state = 173
            self.match(BigTParser.ID_COMP2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





