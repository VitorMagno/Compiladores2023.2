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
        4,1,29,220,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,1,0,
        1,0,1,1,5,1,44,8,1,10,1,12,1,47,9,1,1,1,1,1,1,2,1,2,3,2,53,8,2,1,
        3,1,3,1,3,5,3,58,8,3,10,3,12,3,61,9,3,1,3,1,3,1,4,1,4,1,4,5,4,68,
        8,4,10,4,12,4,71,9,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,
        1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,7,1,7,3,7,93,8,7,1,8,1,8,1,8,1,8,3,
        8,99,8,8,1,8,1,8,1,9,1,9,1,9,1,9,3,9,107,8,9,1,10,1,10,1,10,5,10,
        112,8,10,10,10,12,10,115,9,10,1,10,1,10,1,10,5,10,120,8,10,10,10,
        12,10,123,9,10,1,10,3,10,126,8,10,1,11,1,11,1,11,1,11,1,11,1,11,
        5,11,134,8,11,10,11,12,11,137,9,11,1,11,1,11,1,12,1,12,1,12,1,12,
        1,12,1,12,5,12,147,8,12,10,12,12,12,150,9,12,1,12,1,12,1,13,1,13,
        1,13,1,13,1,13,1,13,3,13,160,8,13,1,13,1,13,1,13,1,13,1,13,1,13,
        1,13,1,13,1,13,1,13,1,13,1,13,5,13,174,8,13,10,13,12,13,177,9,13,
        1,14,1,14,1,14,1,14,5,14,183,8,14,10,14,12,14,186,9,14,1,15,1,15,
        1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,
        1,15,1,15,1,15,1,15,1,15,3,15,208,8,15,1,16,1,16,1,17,1,17,3,17,
        214,8,17,1,18,1,18,1,19,1,19,1,19,0,1,26,20,0,2,4,6,8,10,12,14,16,
        18,20,22,24,26,28,30,32,34,36,38,0,1,1,0,9,10,224,0,40,1,0,0,0,2,
        45,1,0,0,0,4,52,1,0,0,0,6,54,1,0,0,0,8,64,1,0,0,0,10,74,1,0,0,0,
        12,84,1,0,0,0,14,92,1,0,0,0,16,94,1,0,0,0,18,106,1,0,0,0,20,108,
        1,0,0,0,22,127,1,0,0,0,24,140,1,0,0,0,26,159,1,0,0,0,28,178,1,0,
        0,0,30,207,1,0,0,0,32,209,1,0,0,0,34,213,1,0,0,0,36,215,1,0,0,0,
        38,217,1,0,0,0,40,41,3,2,1,0,41,1,1,0,0,0,42,44,3,4,2,0,43,42,1,
        0,0,0,44,47,1,0,0,0,45,43,1,0,0,0,45,46,1,0,0,0,46,48,1,0,0,0,47,
        45,1,0,0,0,48,49,5,0,0,1,49,3,1,0,0,0,50,53,3,6,3,0,51,53,3,8,4,
        0,52,50,1,0,0,0,52,51,1,0,0,0,53,5,1,0,0,0,54,55,5,23,0,0,55,59,
        5,6,0,0,56,58,3,18,9,0,57,56,1,0,0,0,58,61,1,0,0,0,59,57,1,0,0,0,
        59,60,1,0,0,0,60,62,1,0,0,0,61,59,1,0,0,0,62,63,5,7,0,0,63,7,1,0,
        0,0,64,65,5,24,0,0,65,69,5,6,0,0,66,68,3,18,9,0,67,66,1,0,0,0,68,
        71,1,0,0,0,69,67,1,0,0,0,69,70,1,0,0,0,70,72,1,0,0,0,71,69,1,0,0,
        0,72,73,5,7,0,0,73,9,1,0,0,0,74,75,5,21,0,0,75,76,5,4,0,0,76,77,
        3,38,19,0,77,78,5,3,0,0,78,79,3,38,19,0,79,80,5,3,0,0,80,81,3,38,
        19,0,81,82,5,5,0,0,82,83,5,22,0,0,83,11,1,0,0,0,84,85,5,20,0,0,85,
        86,5,4,0,0,86,87,3,38,19,0,87,88,5,5,0,0,88,89,5,22,0,0,89,13,1,
        0,0,0,90,93,3,10,5,0,91,93,3,12,6,0,92,90,1,0,0,0,92,91,1,0,0,0,
        93,15,1,0,0,0,94,95,3,38,19,0,95,98,5,8,0,0,96,99,3,26,13,0,97,99,
        3,28,14,0,98,96,1,0,0,0,98,97,1,0,0,0,99,100,1,0,0,0,100,101,5,22,
        0,0,101,17,1,0,0,0,102,107,3,16,8,0,103,107,3,20,10,0,104,107,3,
        24,12,0,105,107,3,14,7,0,106,102,1,0,0,0,106,103,1,0,0,0,106,104,
        1,0,0,0,106,105,1,0,0,0,107,19,1,0,0,0,108,113,3,22,11,0,109,110,
        5,26,0,0,110,112,3,22,11,0,111,109,1,0,0,0,112,115,1,0,0,0,113,111,
        1,0,0,0,113,114,1,0,0,0,114,125,1,0,0,0,115,113,1,0,0,0,116,117,
        5,26,0,0,117,121,5,6,0,0,118,120,3,18,9,0,119,118,1,0,0,0,120,123,
        1,0,0,0,121,119,1,0,0,0,121,122,1,0,0,0,122,124,1,0,0,0,123,121,
        1,0,0,0,124,126,5,7,0,0,125,116,1,0,0,0,125,126,1,0,0,0,126,21,1,
        0,0,0,127,128,5,25,0,0,128,129,5,4,0,0,129,130,3,28,14,0,130,131,
        5,5,0,0,131,135,5,6,0,0,132,134,3,18,9,0,133,132,1,0,0,0,134,137,
        1,0,0,0,135,133,1,0,0,0,135,136,1,0,0,0,136,138,1,0,0,0,137,135,
        1,0,0,0,138,139,5,7,0,0,139,23,1,0,0,0,140,141,5,27,0,0,141,142,
        5,4,0,0,142,143,3,28,14,0,143,144,5,5,0,0,144,148,5,6,0,0,145,147,
        3,18,9,0,146,145,1,0,0,0,147,150,1,0,0,0,148,146,1,0,0,0,148,149,
        1,0,0,0,149,151,1,0,0,0,150,148,1,0,0,0,151,152,5,7,0,0,152,25,1,
        0,0,0,153,154,6,13,-1,0,154,160,3,34,17,0,155,156,5,4,0,0,156,157,
        3,26,13,0,157,158,5,5,0,0,158,160,1,0,0,0,159,153,1,0,0,0,159,155,
        1,0,0,0,160,175,1,0,0,0,161,162,10,4,0,0,162,163,5,16,0,0,163,174,
        3,26,13,5,164,165,10,3,0,0,165,166,5,17,0,0,166,174,3,26,13,4,167,
        168,10,2,0,0,168,169,5,18,0,0,169,174,3,26,13,3,170,171,10,1,0,0,
        171,172,5,19,0,0,172,174,3,26,13,2,173,161,1,0,0,0,173,164,1,0,0,
        0,173,167,1,0,0,0,173,170,1,0,0,0,174,177,1,0,0,0,175,173,1,0,0,
        0,175,176,1,0,0,0,176,27,1,0,0,0,177,175,1,0,0,0,178,184,3,30,15,
        0,179,180,3,32,16,0,180,181,3,30,15,0,181,183,1,0,0,0,182,179,1,
        0,0,0,183,186,1,0,0,0,184,182,1,0,0,0,184,185,1,0,0,0,185,29,1,0,
        0,0,186,184,1,0,0,0,187,188,3,26,13,0,188,189,5,15,0,0,189,190,3,
        26,13,0,190,208,1,0,0,0,191,192,3,26,13,0,192,193,5,14,0,0,193,194,
        3,26,13,0,194,208,1,0,0,0,195,196,3,26,13,0,196,197,5,11,0,0,197,
        198,3,26,13,0,198,208,1,0,0,0,199,200,3,26,13,0,200,201,5,12,0,0,
        201,202,3,26,13,0,202,208,1,0,0,0,203,204,3,26,13,0,204,205,5,13,
        0,0,205,206,3,26,13,0,206,208,1,0,0,0,207,187,1,0,0,0,207,191,1,
        0,0,0,207,195,1,0,0,0,207,199,1,0,0,0,207,203,1,0,0,0,208,31,1,0,
        0,0,209,210,7,0,0,0,210,33,1,0,0,0,211,214,3,36,18,0,212,214,3,38,
        19,0,213,211,1,0,0,0,213,212,1,0,0,0,214,35,1,0,0,0,215,216,5,28,
        0,0,216,37,1,0,0,0,217,218,5,29,0,0,218,39,1,0,0,0,18,45,52,59,69,
        92,98,106,113,121,125,135,148,159,173,175,184,207,213
    ]

class BigTParser ( Parser ):

    grammarFileName = "BigT.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "','", "'('", 
                     "')'", "'{'", "'}'", "'='", "'&&'", "'||'", "'>='", 
                     "'<='", "'=='", "'<'", "'>'", "'*'", "'/'", "'+'", 
                     "'-'", "'print'", "'chan'", "';'", "'SEQ'", "'PAR'", 
                     "'if'", "'else'", "'while'" ]

    symbolicNames = [ "<INVALID>", "WS", "COMMENT", "VIRG", "AP", "FP", 
                      "AC", "FC", "ASSIGN", "AND", "OR", "GE", "LE", "EQ", 
                      "LT", "GT", "MUL", "DIV", "ADD", "SUB", "PRINT", "CHAN", 
                      "ENDLINE", "SEQ", "PAR", "IF", "ELSE", "WHILE", "INTEGER", 
                      "ID" ]

    RULE_start = 0
    RULE_programa_minipar = 1
    RULE_bloco_stmt = 2
    RULE_bloco_seq = 3
    RULE_bloco_par = 4
    RULE_c_chanel = 5
    RULE_print = 6
    RULE_funcao = 7
    RULE_atribuicao = 8
    RULE_stmts = 9
    RULE_comparacao = 10
    RULE_comparacao_comp = 11
    RULE_repeticao = 12
    RULE_expr = 13
    RULE_comparador = 14
    RULE_comparador_comp = 15
    RULE_comparador_rep = 16
    RULE_fator = 17
    RULE_int = 18
    RULE_id = 19

    ruleNames =  [ "start", "programa_minipar", "bloco_stmt", "bloco_seq", 
                   "bloco_par", "c_chanel", "print", "funcao", "atribuicao", 
                   "stmts", "comparacao", "comparacao_comp", "repeticao", 
                   "expr", "comparador", "comparador_comp", "comparador_rep", 
                   "fator", "int", "id" ]

    EOF = Token.EOF
    WS=1
    COMMENT=2
    VIRG=3
    AP=4
    FP=5
    AC=6
    FC=7
    ASSIGN=8
    AND=9
    OR=10
    GE=11
    LE=12
    EQ=13
    LT=14
    GT=15
    MUL=16
    DIV=17
    ADD=18
    SUB=19
    PRINT=20
    CHAN=21
    ENDLINE=22
    SEQ=23
    PAR=24
    IF=25
    ELSE=26
    WHILE=27
    INTEGER=28
    ID=29

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def programa_minipar(self):
            return self.getTypedRuleContext(BigTParser.Programa_miniparContext,0)


        def getRuleIndex(self):
            return BigTParser.RULE_start

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStart" ):
                return visitor.visitStart(self)
            else:
                return visitor.visitChildren(self)




    def start(self):

        localctx = BigTParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            self.programa_minipar()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Programa_miniparContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(BigTParser.EOF, 0)

        def bloco_stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BigTParser.Bloco_stmtContext)
            else:
                return self.getTypedRuleContext(BigTParser.Bloco_stmtContext,i)


        def getRuleIndex(self):
            return BigTParser.RULE_programa_minipar

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrograma_minipar" ):
                return visitor.visitPrograma_minipar(self)
            else:
                return visitor.visitChildren(self)




    def programa_minipar(self):

        localctx = BigTParser.Programa_miniparContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_programa_minipar)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==23 or _la==24:
                self.state = 42
                self.bloco_stmt()
                self.state = 47
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 48
            self.match(BigTParser.EOF)
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBloco_stmt" ):
                return visitor.visitBloco_stmt(self)
            else:
                return visitor.visitChildren(self)




    def bloco_stmt(self):

        localctx = BigTParser.Bloco_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_bloco_stmt)
        try:
            self.state = 52
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [23]:
                self.enterOuterAlt(localctx, 1)
                self.state = 50
                self.bloco_seq()
                pass
            elif token in [24]:
                self.enterOuterAlt(localctx, 2)
                self.state = 51
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

        def AC(self):
            return self.getToken(BigTParser.AC, 0)

        def FC(self):
            return self.getToken(BigTParser.FC, 0)

        def stmts(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BigTParser.StmtsContext)
            else:
                return self.getTypedRuleContext(BigTParser.StmtsContext,i)


        def getRuleIndex(self):
            return BigTParser.RULE_bloco_seq

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBloco_seq" ):
                return visitor.visitBloco_seq(self)
            else:
                return visitor.visitChildren(self)




    def bloco_seq(self):

        localctx = BigTParser.Bloco_seqContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_bloco_seq)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            self.match(BigTParser.SEQ)
            self.state = 55
            self.match(BigTParser.AC)
            self.state = 59
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 707788800) != 0):
                self.state = 56
                self.stmts()
                self.state = 61
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 62
            self.match(BigTParser.FC)
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

        def AC(self):
            return self.getToken(BigTParser.AC, 0)

        def FC(self):
            return self.getToken(BigTParser.FC, 0)

        def stmts(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BigTParser.StmtsContext)
            else:
                return self.getTypedRuleContext(BigTParser.StmtsContext,i)


        def getRuleIndex(self):
            return BigTParser.RULE_bloco_par

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBloco_par" ):
                return visitor.visitBloco_par(self)
            else:
                return visitor.visitChildren(self)




    def bloco_par(self):

        localctx = BigTParser.Bloco_parContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_bloco_par)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self.match(BigTParser.PAR)
            self.state = 65
            self.match(BigTParser.AC)
            self.state = 69
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 707788800) != 0):
                self.state = 66
                self.stmts()
                self.state = 71
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 72
            self.match(BigTParser.FC)
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


        def getRuleIndex(self):
            return BigTParser.RULE_c_chanel

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ChanContext(C_chanelContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BigTParser.C_chanelContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def CHAN(self):
            return self.getToken(BigTParser.CHAN, 0)
        def AP(self):
            return self.getToken(BigTParser.AP, 0)
        def id_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BigTParser.IdContext)
            else:
                return self.getTypedRuleContext(BigTParser.IdContext,i)

        def VIRG(self, i:int=None):
            if i is None:
                return self.getTokens(BigTParser.VIRG)
            else:
                return self.getToken(BigTParser.VIRG, i)
        def FP(self):
            return self.getToken(BigTParser.FP, 0)
        def ENDLINE(self):
            return self.getToken(BigTParser.ENDLINE, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitChan" ):
                return visitor.visitChan(self)
            else:
                return visitor.visitChildren(self)



    def c_chanel(self):

        localctx = BigTParser.C_chanelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_c_chanel)
        try:
            localctx = BigTParser.ChanContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self.match(BigTParser.CHAN)
            self.state = 75
            self.match(BigTParser.AP)
            self.state = 76
            self.id_()
            self.state = 77
            self.match(BigTParser.VIRG)
            self.state = 78
            self.id_()
            self.state = 79
            self.match(BigTParser.VIRG)
            self.state = 80
            self.id_()
            self.state = 81
            self.match(BigTParser.FP)
            self.state = 82
            self.match(BigTParser.ENDLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return BigTParser.RULE_print

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class PrinContext(PrintContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BigTParser.PrintContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def PRINT(self):
            return self.getToken(BigTParser.PRINT, 0)
        def AP(self):
            return self.getToken(BigTParser.AP, 0)
        def id_(self):
            return self.getTypedRuleContext(BigTParser.IdContext,0)

        def FP(self):
            return self.getToken(BigTParser.FP, 0)
        def ENDLINE(self):
            return self.getToken(BigTParser.ENDLINE, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrin" ):
                return visitor.visitPrin(self)
            else:
                return visitor.visitChildren(self)



    def print_(self):

        localctx = BigTParser.PrintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_print)
        try:
            localctx = BigTParser.PrinContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            self.match(BigTParser.PRINT)
            self.state = 85
            self.match(BigTParser.AP)
            self.state = 86
            self.id_()
            self.state = 87
            self.match(BigTParser.FP)
            self.state = 88
            self.match(BigTParser.ENDLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def c_chanel(self):
            return self.getTypedRuleContext(BigTParser.C_chanelContext,0)


        def print_(self):
            return self.getTypedRuleContext(BigTParser.PrintContext,0)


        def getRuleIndex(self):
            return BigTParser.RULE_funcao

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncao" ):
                return visitor.visitFuncao(self)
            else:
                return visitor.visitChildren(self)




    def funcao(self):

        localctx = BigTParser.FuncaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_funcao)
        try:
            self.state = 92
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [21]:
                self.enterOuterAlt(localctx, 1)
                self.state = 90
                self.c_chanel()
                pass
            elif token in [20]:
                self.enterOuterAlt(localctx, 2)
                self.state = 91
                self.print_()
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

        def id_(self):
            return self.getTypedRuleContext(BigTParser.IdContext,0)


        def ASSIGN(self):
            return self.getToken(BigTParser.ASSIGN, 0)

        def ENDLINE(self):
            return self.getToken(BigTParser.ENDLINE, 0)

        def expr(self):
            return self.getTypedRuleContext(BigTParser.ExprContext,0)


        def comparador(self):
            return self.getTypedRuleContext(BigTParser.ComparadorContext,0)


        def getRuleIndex(self):
            return BigTParser.RULE_atribuicao

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtribuicao" ):
                return visitor.visitAtribuicao(self)
            else:
                return visitor.visitChildren(self)




    def atribuicao(self):

        localctx = BigTParser.AtribuicaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_atribuicao)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            self.id_()
            self.state = 95
            self.match(BigTParser.ASSIGN)
            self.state = 98
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 96
                self.expr(0)
                pass

            elif la_ == 2:
                self.state = 97
                self.comparador()
                pass


            self.state = 100
            self.match(BigTParser.ENDLINE)
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


        def getRuleIndex(self):
            return BigTParser.RULE_stmts

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class CompContext(StmtsContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BigTParser.StmtsContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def comparacao(self):
            return self.getTypedRuleContext(BigTParser.ComparacaoContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComp" ):
                return visitor.visitComp(self)
            else:
                return visitor.visitChildren(self)


    class FuncContext(StmtsContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BigTParser.StmtsContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def funcao(self):
            return self.getTypedRuleContext(BigTParser.FuncaoContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc" ):
                return visitor.visitFunc(self)
            else:
                return visitor.visitChildren(self)


    class RepContext(StmtsContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BigTParser.StmtsContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def repeticao(self):
            return self.getTypedRuleContext(BigTParser.RepeticaoContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRep" ):
                return visitor.visitRep(self)
            else:
                return visitor.visitChildren(self)


    class AtrContext(StmtsContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BigTParser.StmtsContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def atribuicao(self):
            return self.getTypedRuleContext(BigTParser.AtribuicaoContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtr" ):
                return visitor.visitAtr(self)
            else:
                return visitor.visitChildren(self)



    def stmts(self):

        localctx = BigTParser.StmtsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_stmts)
        try:
            self.state = 106
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [29]:
                localctx = BigTParser.AtrContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 102
                self.atribuicao()
                pass
            elif token in [25]:
                localctx = BigTParser.CompContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 103
                self.comparacao()
                pass
            elif token in [27]:
                localctx = BigTParser.RepContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 104
                self.repeticao()
                pass
            elif token in [20, 21]:
                localctx = BigTParser.FuncContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 105
                self.funcao()
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


    class ComparacaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def comparacao_comp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BigTParser.Comparacao_compContext)
            else:
                return self.getTypedRuleContext(BigTParser.Comparacao_compContext,i)


        def ELSE(self, i:int=None):
            if i is None:
                return self.getTokens(BigTParser.ELSE)
            else:
                return self.getToken(BigTParser.ELSE, i)

        def AC(self):
            return self.getToken(BigTParser.AC, 0)

        def FC(self):
            return self.getToken(BigTParser.FC, 0)

        def stmts(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BigTParser.StmtsContext)
            else:
                return self.getTypedRuleContext(BigTParser.StmtsContext,i)


        def getRuleIndex(self):
            return BigTParser.RULE_comparacao

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComparacao" ):
                return visitor.visitComparacao(self)
            else:
                return visitor.visitChildren(self)




    def comparacao(self):

        localctx = BigTParser.ComparacaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_comparacao)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 108
            self.comparacao_comp()
            self.state = 113
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 109
                    self.match(BigTParser.ELSE)
                    self.state = 110
                    self.comparacao_comp() 
                self.state = 115
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

            self.state = 125
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==26:
                self.state = 116
                self.match(BigTParser.ELSE)
                self.state = 117
                self.match(BigTParser.AC)
                self.state = 121
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 707788800) != 0):
                    self.state = 118
                    self.stmts()
                    self.state = 123
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 124
                self.match(BigTParser.FC)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Comparacao_compContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(BigTParser.IF, 0)

        def AP(self):
            return self.getToken(BigTParser.AP, 0)

        def comparador(self):
            return self.getTypedRuleContext(BigTParser.ComparadorContext,0)


        def FP(self):
            return self.getToken(BigTParser.FP, 0)

        def AC(self):
            return self.getToken(BigTParser.AC, 0)

        def FC(self):
            return self.getToken(BigTParser.FC, 0)

        def stmts(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BigTParser.StmtsContext)
            else:
                return self.getTypedRuleContext(BigTParser.StmtsContext,i)


        def getRuleIndex(self):
            return BigTParser.RULE_comparacao_comp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComparacao_comp" ):
                return visitor.visitComparacao_comp(self)
            else:
                return visitor.visitChildren(self)




    def comparacao_comp(self):

        localctx = BigTParser.Comparacao_compContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_comparacao_comp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 127
            self.match(BigTParser.IF)
            self.state = 128
            self.match(BigTParser.AP)
            self.state = 129
            self.comparador()
            self.state = 130
            self.match(BigTParser.FP)
            self.state = 131
            self.match(BigTParser.AC)
            self.state = 135
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 707788800) != 0):
                self.state = 132
                self.stmts()
                self.state = 137
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 138
            self.match(BigTParser.FC)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RepeticaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(BigTParser.WHILE, 0)

        def AP(self):
            return self.getToken(BigTParser.AP, 0)

        def comparador(self):
            return self.getTypedRuleContext(BigTParser.ComparadorContext,0)


        def FP(self):
            return self.getToken(BigTParser.FP, 0)

        def AC(self):
            return self.getToken(BigTParser.AC, 0)

        def FC(self):
            return self.getToken(BigTParser.FC, 0)

        def stmts(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BigTParser.StmtsContext)
            else:
                return self.getTypedRuleContext(BigTParser.StmtsContext,i)


        def getRuleIndex(self):
            return BigTParser.RULE_repeticao

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRepeticao" ):
                return visitor.visitRepeticao(self)
            else:
                return visitor.visitChildren(self)




    def repeticao(self):

        localctx = BigTParser.RepeticaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_repeticao)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 140
            self.match(BigTParser.WHILE)
            self.state = 141
            self.match(BigTParser.AP)
            self.state = 142
            self.comparador()
            self.state = 143
            self.match(BigTParser.FP)
            self.state = 144
            self.match(BigTParser.AC)
            self.state = 148
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 707788800) != 0):
                self.state = 145
                self.stmts()
                self.state = 150
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 151
            self.match(BigTParser.FC)
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
            return BigTParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class DIVContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BigTParser.ExprContext
            super().__init__(parser)
            self.left = None # ExprContext
            self.right = None # ExprContext
            self.copyFrom(ctx)

        def DIV(self):
            return self.getToken(BigTParser.DIV, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BigTParser.ExprContext)
            else:
                return self.getTypedRuleContext(BigTParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDIV" ):
                return visitor.visitDIV(self)
            else:
                return visitor.visitChildren(self)


    class ADDContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BigTParser.ExprContext
            super().__init__(parser)
            self.left = None # ExprContext
            self.right = None # ExprContext
            self.copyFrom(ctx)

        def ADD(self):
            return self.getToken(BigTParser.ADD, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BigTParser.ExprContext)
            else:
                return self.getTypedRuleContext(BigTParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitADD" ):
                return visitor.visitADD(self)
            else:
                return visitor.visitChildren(self)


    class SUBContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BigTParser.ExprContext
            super().__init__(parser)
            self.left = None # ExprContext
            self.right = None # ExprContext
            self.copyFrom(ctx)

        def SUB(self):
            return self.getToken(BigTParser.SUB, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BigTParser.ExprContext)
            else:
                return self.getTypedRuleContext(BigTParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSUB" ):
                return visitor.visitSUB(self)
            else:
                return visitor.visitChildren(self)


    class MULContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BigTParser.ExprContext
            super().__init__(parser)
            self.left = None # ExprContext
            self.right = None # ExprContext
            self.copyFrom(ctx)

        def MUL(self):
            return self.getToken(BigTParser.MUL, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BigTParser.ExprContext)
            else:
                return self.getTypedRuleContext(BigTParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMUL" ):
                return visitor.visitMUL(self)
            else:
                return visitor.visitChildren(self)


    class SimpleAtr2Context(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BigTParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def fator(self):
            return self.getTypedRuleContext(BigTParser.FatorContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSimpleAtr2" ):
                return visitor.visitSimpleAtr2(self)
            else:
                return visitor.visitChildren(self)


    class ParenexprParenContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BigTParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def AP(self):
            return self.getToken(BigTParser.AP, 0)
        def expr(self):
            return self.getTypedRuleContext(BigTParser.ExprContext,0)

        def FP(self):
            return self.getToken(BigTParser.FP, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParenexprParen" ):
                return visitor.visitParenexprParen(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BigTParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 26
        self.enterRecursionRule(localctx, 26, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 159
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [28, 29]:
                localctx = BigTParser.SimpleAtr2Context(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 154
                self.fator()
                pass
            elif token in [4]:
                localctx = BigTParser.ParenexprParenContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 155
                self.match(BigTParser.AP)
                self.state = 156
                self.expr(0)
                self.state = 157
                self.match(BigTParser.FP)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 175
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 173
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
                    if la_ == 1:
                        localctx = BigTParser.MULContext(self, BigTParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 161
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 162
                        self.match(BigTParser.MUL)
                        self.state = 163
                        localctx.right = self.expr(5)
                        pass

                    elif la_ == 2:
                        localctx = BigTParser.DIVContext(self, BigTParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 164
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 165
                        self.match(BigTParser.DIV)
                        self.state = 166
                        localctx.right = self.expr(4)
                        pass

                    elif la_ == 3:
                        localctx = BigTParser.ADDContext(self, BigTParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 167
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 168
                        self.match(BigTParser.ADD)
                        self.state = 169
                        localctx.right = self.expr(3)
                        pass

                    elif la_ == 4:
                        localctx = BigTParser.SUBContext(self, BigTParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 170
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 171
                        self.match(BigTParser.SUB)
                        self.state = 172
                        localctx.right = self.expr(2)
                        pass

             
                self.state = 177
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ComparadorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def comparador_comp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BigTParser.Comparador_compContext)
            else:
                return self.getTypedRuleContext(BigTParser.Comparador_compContext,i)


        def comparador_rep(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BigTParser.Comparador_repContext)
            else:
                return self.getTypedRuleContext(BigTParser.Comparador_repContext,i)


        def getRuleIndex(self):
            return BigTParser.RULE_comparador

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComparador" ):
                return visitor.visitComparador(self)
            else:
                return visitor.visitChildren(self)




    def comparador(self):

        localctx = BigTParser.ComparadorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_comparador)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 178
            self.comparador_comp()
            self.state = 184
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==9 or _la==10:
                self.state = 179
                self.comparador_rep()
                self.state = 180
                self.comparador_comp()
                self.state = 186
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Comparador_compContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return BigTParser.RULE_comparador_comp

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class LTContext(Comparador_compContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BigTParser.Comparador_compContext
            super().__init__(parser)
            self.left = None # ExprContext
            self.right = None # ExprContext
            self.copyFrom(ctx)

        def LT(self):
            return self.getToken(BigTParser.LT, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BigTParser.ExprContext)
            else:
                return self.getTypedRuleContext(BigTParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLT" ):
                return visitor.visitLT(self)
            else:
                return visitor.visitChildren(self)


    class LEContext(Comparador_compContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BigTParser.Comparador_compContext
            super().__init__(parser)
            self.left = None # ExprContext
            self.right = None # ExprContext
            self.copyFrom(ctx)

        def LE(self):
            return self.getToken(BigTParser.LE, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BigTParser.ExprContext)
            else:
                return self.getTypedRuleContext(BigTParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLE" ):
                return visitor.visitLE(self)
            else:
                return visitor.visitChildren(self)


    class EQContext(Comparador_compContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BigTParser.Comparador_compContext
            super().__init__(parser)
            self.left = None # ExprContext
            self.right = None # ExprContext
            self.copyFrom(ctx)

        def EQ(self):
            return self.getToken(BigTParser.EQ, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BigTParser.ExprContext)
            else:
                return self.getTypedRuleContext(BigTParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEQ" ):
                return visitor.visitEQ(self)
            else:
                return visitor.visitChildren(self)


    class GTContext(Comparador_compContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BigTParser.Comparador_compContext
            super().__init__(parser)
            self.left = None # ExprContext
            self.right = None # ExprContext
            self.copyFrom(ctx)

        def GT(self):
            return self.getToken(BigTParser.GT, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BigTParser.ExprContext)
            else:
                return self.getTypedRuleContext(BigTParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGT" ):
                return visitor.visitGT(self)
            else:
                return visitor.visitChildren(self)


    class GEContext(Comparador_compContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BigTParser.Comparador_compContext
            super().__init__(parser)
            self.left = None # ExprContext
            self.right = None # ExprContext
            self.copyFrom(ctx)

        def GE(self):
            return self.getToken(BigTParser.GE, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BigTParser.ExprContext)
            else:
                return self.getTypedRuleContext(BigTParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGE" ):
                return visitor.visitGE(self)
            else:
                return visitor.visitChildren(self)



    def comparador_comp(self):

        localctx = BigTParser.Comparador_compContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_comparador_comp)
        try:
            self.state = 207
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                localctx = BigTParser.GTContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 187
                localctx.left = self.expr(0)
                self.state = 188
                self.match(BigTParser.GT)
                self.state = 189
                localctx.right = self.expr(0)
                pass

            elif la_ == 2:
                localctx = BigTParser.LTContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 191
                localctx.left = self.expr(0)
                self.state = 192
                self.match(BigTParser.LT)
                self.state = 193
                localctx.right = self.expr(0)
                pass

            elif la_ == 3:
                localctx = BigTParser.GEContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 195
                localctx.left = self.expr(0)
                self.state = 196
                self.match(BigTParser.GE)
                self.state = 197
                localctx.right = self.expr(0)
                pass

            elif la_ == 4:
                localctx = BigTParser.LEContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 199
                localctx.left = self.expr(0)
                self.state = 200
                self.match(BigTParser.LE)
                self.state = 201
                localctx.right = self.expr(0)
                pass

            elif la_ == 5:
                localctx = BigTParser.EQContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 203
                localctx.left = self.expr(0)
                self.state = 204
                self.match(BigTParser.EQ)
                self.state = 205
                localctx.right = self.expr(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Comparador_repContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AND(self):
            return self.getToken(BigTParser.AND, 0)

        def OR(self):
            return self.getToken(BigTParser.OR, 0)

        def getRuleIndex(self):
            return BigTParser.RULE_comparador_rep

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComparador_rep" ):
                return visitor.visitComparador_rep(self)
            else:
                return visitor.visitChildren(self)




    def comparador_rep(self):

        localctx = BigTParser.Comparador_repContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_comparador_rep)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 209
            _la = self._input.LA(1)
            if not(_la==9 or _la==10):
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


    class FatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def int_(self):
            return self.getTypedRuleContext(BigTParser.IntContext,0)


        def id_(self):
            return self.getTypedRuleContext(BigTParser.IdContext,0)


        def getRuleIndex(self):
            return BigTParser.RULE_fator

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFator" ):
                return visitor.visitFator(self)
            else:
                return visitor.visitChildren(self)




    def fator(self):

        localctx = BigTParser.FatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_fator)
        try:
            self.state = 213
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [28]:
                self.enterOuterAlt(localctx, 1)
                self.state = 211
                self.int_()
                pass
            elif token in [29]:
                self.enterOuterAlt(localctx, 2)
                self.state = 212
                self.id_()
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


    class IntContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER(self):
            return self.getToken(BigTParser.INTEGER, 0)

        def getRuleIndex(self):
            return BigTParser.RULE_int

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInt" ):
                return visitor.visitInt(self)
            else:
                return visitor.visitChildren(self)




    def int_(self):

        localctx = BigTParser.IntContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_int)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 215
            self.match(BigTParser.INTEGER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BigTParser.ID, 0)

        def getRuleIndex(self):
            return BigTParser.RULE_id

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitId" ):
                return visitor.visitId(self)
            else:
                return visitor.visitChildren(self)




    def id_(self):

        localctx = BigTParser.IdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_id)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 217
            self.match(BigTParser.ID)
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
        self._predicates[13] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 1)
         




