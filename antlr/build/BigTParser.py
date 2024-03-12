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
        4,1,29,171,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,1,0,1,0,1,1,1,1,3,1,41,8,
        1,1,2,1,2,1,2,1,3,1,3,1,3,1,4,1,4,3,4,51,8,4,1,5,1,5,3,5,55,8,5,
        1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,71,8,
        6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,3,7,87,
        8,7,1,8,1,8,3,8,91,8,8,1,9,1,9,1,9,1,9,1,10,1,10,1,10,1,11,1,11,
        1,11,3,11,103,8,11,1,11,1,11,1,11,3,11,108,8,11,1,11,1,11,1,11,3,
        11,113,8,11,1,11,1,11,1,11,3,11,118,8,11,1,11,1,11,1,11,3,11,123,
        8,11,3,11,125,8,11,1,12,1,12,1,12,1,13,1,13,1,13,3,13,133,8,13,1,
        13,1,13,1,13,3,13,138,8,13,3,13,140,8,13,1,14,1,14,3,14,144,8,14,
        1,15,1,15,1,15,3,15,149,8,15,1,15,1,15,1,15,3,15,154,8,15,3,15,156,
        8,15,1,16,1,16,1,16,1,16,1,16,1,16,3,16,164,8,16,1,17,1,17,1,17,
        1,17,1,17,1,17,0,0,18,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,
        32,34,0,0,176,0,36,1,0,0,0,2,40,1,0,0,0,4,42,1,0,0,0,6,45,1,0,0,
        0,8,50,1,0,0,0,10,54,1,0,0,0,12,70,1,0,0,0,14,86,1,0,0,0,16,90,1,
        0,0,0,18,92,1,0,0,0,20,96,1,0,0,0,22,124,1,0,0,0,24,126,1,0,0,0,
        26,139,1,0,0,0,28,141,1,0,0,0,30,155,1,0,0,0,32,163,1,0,0,0,34,165,
        1,0,0,0,36,37,3,2,1,0,37,1,1,0,0,0,38,41,3,4,2,0,39,41,3,6,3,0,40,
        38,1,0,0,0,40,39,1,0,0,0,41,3,1,0,0,0,42,43,5,26,0,0,43,44,3,8,4,
        0,44,5,1,0,0,0,45,46,5,27,0,0,46,47,3,8,4,0,47,7,1,0,0,0,48,51,3,
        18,9,0,49,51,3,10,5,0,50,48,1,0,0,0,50,49,1,0,0,0,51,9,1,0,0,0,52,
        55,3,12,6,0,53,55,3,14,7,0,54,52,1,0,0,0,54,53,1,0,0,0,55,11,1,0,
        0,0,56,57,5,4,0,0,57,58,5,1,0,0,58,59,3,20,10,0,59,60,5,2,0,0,60,
        61,3,12,6,0,61,62,5,5,0,0,62,63,3,12,6,0,63,71,1,0,0,0,64,65,5,6,
        0,0,65,66,5,1,0,0,66,67,3,20,10,0,67,68,5,2,0,0,68,69,3,10,5,0,69,
        71,1,0,0,0,70,56,1,0,0,0,70,64,1,0,0,0,71,13,1,0,0,0,72,73,5,4,0,
        0,73,74,5,1,0,0,74,75,3,20,10,0,75,76,5,2,0,0,76,77,3,10,5,0,77,
        87,1,0,0,0,78,79,5,4,0,0,79,80,5,1,0,0,80,81,3,20,10,0,81,82,5,2,
        0,0,82,83,3,12,6,0,83,84,5,5,0,0,84,85,3,14,7,0,85,87,1,0,0,0,86,
        72,1,0,0,0,86,78,1,0,0,0,87,15,1,0,0,0,88,91,5,28,0,0,89,91,5,19,
        0,0,90,88,1,0,0,0,90,89,1,0,0,0,91,17,1,0,0,0,92,93,5,20,0,0,93,
        94,5,3,0,0,94,95,3,24,12,0,95,19,1,0,0,0,96,97,3,28,14,0,97,98,3,
        22,11,0,98,21,1,0,0,0,99,100,5,10,0,0,100,102,3,28,14,0,101,103,
        3,22,11,0,102,101,1,0,0,0,102,103,1,0,0,0,103,125,1,0,0,0,104,105,
        5,11,0,0,105,107,3,28,14,0,106,108,3,22,11,0,107,106,1,0,0,0,107,
        108,1,0,0,0,108,125,1,0,0,0,109,110,5,12,0,0,110,112,3,28,14,0,111,
        113,3,22,11,0,112,111,1,0,0,0,112,113,1,0,0,0,113,125,1,0,0,0,114,
        115,5,13,0,0,115,117,3,28,14,0,116,118,3,22,11,0,117,116,1,0,0,0,
        117,118,1,0,0,0,118,125,1,0,0,0,119,120,5,14,0,0,120,122,3,28,14,
        0,121,123,3,22,11,0,122,121,1,0,0,0,122,123,1,0,0,0,123,125,1,0,
        0,0,124,99,1,0,0,0,124,104,1,0,0,0,124,109,1,0,0,0,124,114,1,0,0,
        0,124,119,1,0,0,0,125,23,1,0,0,0,126,127,3,28,14,0,127,128,3,26,
        13,0,128,25,1,0,0,0,129,130,5,17,0,0,130,132,3,28,14,0,131,133,3,
        26,13,0,132,131,1,0,0,0,132,133,1,0,0,0,133,140,1,0,0,0,134,135,
        5,18,0,0,135,137,3,28,14,0,136,138,3,26,13,0,137,136,1,0,0,0,137,
        138,1,0,0,0,138,140,1,0,0,0,139,129,1,0,0,0,139,134,1,0,0,0,140,
        27,1,0,0,0,141,143,3,32,16,0,142,144,3,30,15,0,143,142,1,0,0,0,143,
        144,1,0,0,0,144,29,1,0,0,0,145,146,5,15,0,0,146,148,3,32,16,0,147,
        149,3,30,15,0,148,147,1,0,0,0,148,149,1,0,0,0,149,156,1,0,0,0,150,
        151,5,16,0,0,151,153,3,32,16,0,152,154,3,30,15,0,153,152,1,0,0,0,
        153,154,1,0,0,0,154,156,1,0,0,0,155,145,1,0,0,0,155,150,1,0,0,0,
        156,31,1,0,0,0,157,164,5,21,0,0,158,164,5,20,0,0,159,160,5,1,0,0,
        160,161,3,24,12,0,161,162,5,2,0,0,162,164,1,0,0,0,163,157,1,0,0,
        0,163,158,1,0,0,0,163,159,1,0,0,0,164,33,1,0,0,0,165,166,5,22,0,
        0,166,167,5,20,0,0,167,168,5,23,0,0,168,169,5,24,0,0,169,35,1,0,
        0,0,20,40,50,54,70,86,90,102,107,112,117,122,124,132,137,139,143,
        148,153,155,163
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


        def getRuleIndex(self):
            return BigTParser.RULE_progama_minipar

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgama_minipar" ):
                listener.enterProgama_minipar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgama_minipar" ):
                listener.exitProgama_minipar(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgama_minipar" ):
                return visitor.visitProgama_minipar(self)
            else:
                return visitor.visitChildren(self)




    def progama_minipar(self):

        localctx = BigTParser.Progama_miniparContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_progama_minipar)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            self.bloco_stmt()
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBloco_stmt" ):
                return visitor.visitBloco_stmt(self)
            else:
                return visitor.visitChildren(self)




    def bloco_stmt(self):

        localctx = BigTParser.Bloco_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_bloco_stmt)
        try:
            self.state = 40
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [26]:
                self.enterOuterAlt(localctx, 1)
                self.state = 38
                self.bloco_seq()
                pass
            elif token in [27]:
                self.enterOuterAlt(localctx, 2)
                self.state = 39
                self.bloco_par()
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBloco_seq" ):
                return visitor.visitBloco_seq(self)
            else:
                return visitor.visitChildren(self)




    def bloco_seq(self):

        localctx = BigTParser.Bloco_seqContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_bloco_seq)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self.match(BigTParser.SEQ)
            self.state = 43
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBloco_par" ):
                return visitor.visitBloco_par(self)
            else:
                return visitor.visitChildren(self)




    def bloco_par(self):

        localctx = BigTParser.Bloco_parContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_bloco_par)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            self.match(BigTParser.PAR)
            self.state = 46
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmts" ):
                return visitor.visitStmts(self)
            else:
                return visitor.visitChildren(self)




    def stmts(self):

        localctx = BigTParser.StmtsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_stmts)
        try:
            self.state = 50
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [20]:
                self.enterOuterAlt(localctx, 1)
                self.state = 48
                self.atribuicao()
                pass
            elif token in [4, 6]:
                self.enterOuterAlt(localctx, 2)
                self.state = 49
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = BigTParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_stmt)
        try:
            self.state = 54
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 52
                self.cmd_a()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 53
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWHILE" ):
                return visitor.visitWHILE(self)
            else:
                return visitor.visitChildren(self)


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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIFelse" ):
                return visitor.visitIFelse(self)
            else:
                return visitor.visitChildren(self)



    def cmd_a(self):

        localctx = BigTParser.Cmd_aContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_cmd_a)
        try:
            self.state = 70
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4]:
                localctx = BigTParser.IFelseContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 56
                self.match(BigTParser.IF)
                self.state = 57
                self.match(BigTParser.T__0)
                self.state = 58
                self.bool_()
                self.state = 59
                self.match(BigTParser.T__1)
                self.state = 60
                self.cmd_a()
                self.state = 61
                self.match(BigTParser.ELSE)
                self.state = 62
                self.cmd_a()
                pass
            elif token in [6]:
                localctx = BigTParser.WHILEContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 64
                self.match(BigTParser.WHILE)
                self.state = 65
                self.match(BigTParser.T__0)
                self.state = 66
                self.bool_()
                self.state = 67
                self.match(BigTParser.T__1)
                self.state = 68
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIFelsena" ):
                return visitor.visitIFelsena(self)
            else:
                return visitor.visitChildren(self)


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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIF" ):
                return visitor.visitIF(self)
            else:
                return visitor.visitChildren(self)



    def cmd_na(self):

        localctx = BigTParser.Cmd_naContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_cmd_na)
        try:
            self.state = 86
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                localctx = BigTParser.IFContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 72
                self.match(BigTParser.IF)
                self.state = 73
                self.match(BigTParser.T__0)
                self.state = 74
                self.bool_()
                self.state = 75
                self.match(BigTParser.T__1)
                self.state = 76
                self.stmt()
                pass

            elif la_ == 2:
                localctx = BigTParser.IFelsenaContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 78
                self.match(BigTParser.IF)
                self.state = 79
                self.match(BigTParser.T__0)
                self.state = 80
                self.bool_()
                self.state = 81
                self.match(BigTParser.T__1)
                self.state = 82
                self.cmd_a()
                self.state = 83
                self.match(BigTParser.ELSE)
                self.state = 84
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCHAR" ):
                return visitor.visitCHAR(self)
            else:
                return visitor.visitChildren(self)


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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitINT" ):
                return visitor.visitINT(self)
            else:
                return visitor.visitChildren(self)



    def tipos_var(self):

        localctx = BigTParser.Tipos_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_tipos_var)
        try:
            self.state = 90
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [28]:
                localctx = BigTParser.INTContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 88
                self.match(BigTParser.INT)
                pass
            elif token in [19]:
                localctx = BigTParser.CHARContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 89
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtribuicao" ):
                return visitor.visitAtribuicao(self)
            else:
                return visitor.visitChildren(self)




    def atribuicao(self):

        localctx = BigTParser.AtribuicaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_atribuicao)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 92
            self.match(BigTParser.ID)
            self.state = 93
            self.match(BigTParser.T__2)
            self.state = 94
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBool" ):
                return visitor.visitBool(self)
            else:
                return visitor.visitChildren(self)




    def bool_(self):

        localctx = BigTParser.BoolContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_bool)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            self.termo()
            self.state = 97
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLT" ):
                return visitor.visitLT(self)
            else:
                return visitor.visitChildren(self)


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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLE" ):
                return visitor.visitLE(self)
            else:
                return visitor.visitChildren(self)


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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEQ" ):
                return visitor.visitEQ(self)
            else:
                return visitor.visitChildren(self)


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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGT" ):
                return visitor.visitGT(self)
            else:
                return visitor.visitChildren(self)


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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGE" ):
                return visitor.visitGE(self)
            else:
                return visitor.visitChildren(self)



    def mais_bool(self):

        localctx = BigTParser.Mais_boolContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_mais_bool)
        self._la = 0 # Token type
        try:
            self.state = 124
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                localctx = BigTParser.GEContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 99
                self.match(BigTParser.GE)
                self.state = 100
                self.termo()
                self.state = 102
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 31744) != 0):
                    self.state = 101
                    self.mais_bool()


                pass
            elif token in [11]:
                localctx = BigTParser.LEContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 104
                self.match(BigTParser.LE)
                self.state = 105
                self.termo()
                self.state = 107
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 31744) != 0):
                    self.state = 106
                    self.mais_bool()


                pass
            elif token in [12]:
                localctx = BigTParser.EQContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 109
                self.match(BigTParser.EQ)
                self.state = 110
                self.termo()
                self.state = 112
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 31744) != 0):
                    self.state = 111
                    self.mais_bool()


                pass
            elif token in [13]:
                localctx = BigTParser.LTContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 114
                self.match(BigTParser.LT)
                self.state = 115
                self.termo()
                self.state = 117
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 31744) != 0):
                    self.state = 116
                    self.mais_bool()


                pass
            elif token in [14]:
                localctx = BigTParser.GTContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 119
                self.match(BigTParser.GT)
                self.state = 120
                self.termo()
                self.state = 122
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 31744) != 0):
                    self.state = 121
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = BigTParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 126
            self.termo()
            self.state = 127
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitADD" ):
                return visitor.visitADD(self)
            else:
                return visitor.visitChildren(self)


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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSUB" ):
                return visitor.visitSUB(self)
            else:
                return visitor.visitChildren(self)



    def mais_expr(self):

        localctx = BigTParser.Mais_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_mais_expr)
        self._la = 0 # Token type
        try:
            self.state = 139
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [17]:
                localctx = BigTParser.ADDContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 129
                self.match(BigTParser.ADD)
                self.state = 130
                self.termo()
                self.state = 132
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==17 or _la==18:
                    self.state = 131
                    self.mais_expr()


                pass
            elif token in [18]:
                localctx = BigTParser.SUBContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 134
                self.match(BigTParser.SUB)
                self.state = 135
                self.termo()
                self.state = 137
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==17 or _la==18:
                    self.state = 136
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTermo" ):
                return visitor.visitTermo(self)
            else:
                return visitor.visitChildren(self)




    def termo(self):

        localctx = BigTParser.TermoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_termo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 141
            self.fator()
            self.state = 143
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==15 or _la==16:
                self.state = 142
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDIV" ):
                return visitor.visitDIV(self)
            else:
                return visitor.visitChildren(self)


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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMUL" ):
                return visitor.visitMUL(self)
            else:
                return visitor.visitChildren(self)



    def mais_termo(self):

        localctx = BigTParser.Mais_termoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_mais_termo)
        self._la = 0 # Token type
        try:
            self.state = 155
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [15]:
                localctx = BigTParser.MULContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 145
                self.match(BigTParser.MUL)
                self.state = 146
                self.fator()
                self.state = 148
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==15 or _la==16:
                    self.state = 147
                    self.mais_termo()


                pass
            elif token in [16]:
                localctx = BigTParser.DIVContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 150
                self.match(BigTParser.DIV)
                self.state = 151
                self.fator()
                self.state = 153
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==15 or _la==16:
                    self.state = 152
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParenexprParen" ):
                return visitor.visitParenexprParen(self)
            else:
                return visitor.visitChildren(self)


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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitID" ):
                return visitor.visitID(self)
            else:
                return visitor.visitChildren(self)


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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDIGIT" ):
                return visitor.visitDIGIT(self)
            else:
                return visitor.visitChildren(self)



    def fator(self):

        localctx = BigTParser.FatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_fator)
        try:
            self.state = 163
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [21]:
                localctx = BigTParser.DIGITContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 157
                self.match(BigTParser.DIGIT)
                pass
            elif token in [20]:
                localctx = BigTParser.IDContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 158
                self.match(BigTParser.ID)
                pass
            elif token in [1]:
                localctx = BigTParser.ParenexprParenContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 159
                self.match(BigTParser.T__0)
                self.state = 160
                self.expr()
                self.state = 161
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitC_chanel" ):
                return visitor.visitC_chanel(self)
            else:
                return visitor.visitChildren(self)




    def c_chanel(self):

        localctx = BigTParser.C_chanelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_c_chanel)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 165
            self.match(BigTParser.CHAN)
            self.state = 166
            self.match(BigTParser.ID)
            self.state = 167
            self.match(BigTParser.ID_COMP1)
            self.state = 168
            self.match(BigTParser.ID_COMP2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





