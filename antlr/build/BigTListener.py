# Generated from BigT.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .BigTParser import BigTParser
else:
    from BigTParser import BigTParser

# This class defines a complete listener for a parse tree produced by BigTParser.
class BigTListener(ParseTreeListener):

    # Enter a parse tree produced by BigTParser#progama_minipar.
    def enterProgama_minipar(self, ctx:BigTParser.Progama_miniparContext):
        pass

    # Exit a parse tree produced by BigTParser#progama_minipar.
    def exitProgama_minipar(self, ctx:BigTParser.Progama_miniparContext):
        pass


    # Enter a parse tree produced by BigTParser#bloco_stmt.
    def enterBloco_stmt(self, ctx:BigTParser.Bloco_stmtContext):
        pass

    # Exit a parse tree produced by BigTParser#bloco_stmt.
    def exitBloco_stmt(self, ctx:BigTParser.Bloco_stmtContext):
        pass


    # Enter a parse tree produced by BigTParser#bloco_seq.
    def enterBloco_seq(self, ctx:BigTParser.Bloco_seqContext):
        pass

    # Exit a parse tree produced by BigTParser#bloco_seq.
    def exitBloco_seq(self, ctx:BigTParser.Bloco_seqContext):
        pass


    # Enter a parse tree produced by BigTParser#bloco_par.
    def enterBloco_par(self, ctx:BigTParser.Bloco_parContext):
        pass

    # Exit a parse tree produced by BigTParser#bloco_par.
    def exitBloco_par(self, ctx:BigTParser.Bloco_parContext):
        pass


    # Enter a parse tree produced by BigTParser#stmts.
    def enterStmts(self, ctx:BigTParser.StmtsContext):
        pass

    # Exit a parse tree produced by BigTParser#stmts.
    def exitStmts(self, ctx:BigTParser.StmtsContext):
        pass


    # Enter a parse tree produced by BigTParser#stmt.
    def enterStmt(self, ctx:BigTParser.StmtContext):
        pass

    # Exit a parse tree produced by BigTParser#stmt.
    def exitStmt(self, ctx:BigTParser.StmtContext):
        pass


    # Enter a parse tree produced by BigTParser#IFelse.
    def enterIFelse(self, ctx:BigTParser.IFelseContext):
        pass

    # Exit a parse tree produced by BigTParser#IFelse.
    def exitIFelse(self, ctx:BigTParser.IFelseContext):
        pass


    # Enter a parse tree produced by BigTParser#WHILE.
    def enterWHILE(self, ctx:BigTParser.WHILEContext):
        pass

    # Exit a parse tree produced by BigTParser#WHILE.
    def exitWHILE(self, ctx:BigTParser.WHILEContext):
        pass


    # Enter a parse tree produced by BigTParser#IF.
    def enterIF(self, ctx:BigTParser.IFContext):
        pass

    # Exit a parse tree produced by BigTParser#IF.
    def exitIF(self, ctx:BigTParser.IFContext):
        pass


    # Enter a parse tree produced by BigTParser#IFelsena.
    def enterIFelsena(self, ctx:BigTParser.IFelsenaContext):
        pass

    # Exit a parse tree produced by BigTParser#IFelsena.
    def exitIFelsena(self, ctx:BigTParser.IFelsenaContext):
        pass


    # Enter a parse tree produced by BigTParser#INT.
    def enterINT(self, ctx:BigTParser.INTContext):
        pass

    # Exit a parse tree produced by BigTParser#INT.
    def exitINT(self, ctx:BigTParser.INTContext):
        pass


    # Enter a parse tree produced by BigTParser#CHAR.
    def enterCHAR(self, ctx:BigTParser.CHARContext):
        pass

    # Exit a parse tree produced by BigTParser#CHAR.
    def exitCHAR(self, ctx:BigTParser.CHARContext):
        pass


    # Enter a parse tree produced by BigTParser#atribuicao.
    def enterAtribuicao(self, ctx:BigTParser.AtribuicaoContext):
        pass

    # Exit a parse tree produced by BigTParser#atribuicao.
    def exitAtribuicao(self, ctx:BigTParser.AtribuicaoContext):
        pass


    # Enter a parse tree produced by BigTParser#bool.
    def enterBool(self, ctx:BigTParser.BoolContext):
        pass

    # Exit a parse tree produced by BigTParser#bool.
    def exitBool(self, ctx:BigTParser.BoolContext):
        pass


    # Enter a parse tree produced by BigTParser#GE.
    def enterGE(self, ctx:BigTParser.GEContext):
        pass

    # Exit a parse tree produced by BigTParser#GE.
    def exitGE(self, ctx:BigTParser.GEContext):
        pass


    # Enter a parse tree produced by BigTParser#LE.
    def enterLE(self, ctx:BigTParser.LEContext):
        pass

    # Exit a parse tree produced by BigTParser#LE.
    def exitLE(self, ctx:BigTParser.LEContext):
        pass


    # Enter a parse tree produced by BigTParser#EQ.
    def enterEQ(self, ctx:BigTParser.EQContext):
        pass

    # Exit a parse tree produced by BigTParser#EQ.
    def exitEQ(self, ctx:BigTParser.EQContext):
        pass


    # Enter a parse tree produced by BigTParser#LT.
    def enterLT(self, ctx:BigTParser.LTContext):
        pass

    # Exit a parse tree produced by BigTParser#LT.
    def exitLT(self, ctx:BigTParser.LTContext):
        pass


    # Enter a parse tree produced by BigTParser#GT.
    def enterGT(self, ctx:BigTParser.GTContext):
        pass

    # Exit a parse tree produced by BigTParser#GT.
    def exitGT(self, ctx:BigTParser.GTContext):
        pass


    # Enter a parse tree produced by BigTParser#expr.
    def enterExpr(self, ctx:BigTParser.ExprContext):
        pass

    # Exit a parse tree produced by BigTParser#expr.
    def exitExpr(self, ctx:BigTParser.ExprContext):
        pass


    # Enter a parse tree produced by BigTParser#ADD.
    def enterADD(self, ctx:BigTParser.ADDContext):
        pass

    # Exit a parse tree produced by BigTParser#ADD.
    def exitADD(self, ctx:BigTParser.ADDContext):
        pass


    # Enter a parse tree produced by BigTParser#SUB.
    def enterSUB(self, ctx:BigTParser.SUBContext):
        pass

    # Exit a parse tree produced by BigTParser#SUB.
    def exitSUB(self, ctx:BigTParser.SUBContext):
        pass


    # Enter a parse tree produced by BigTParser#termo.
    def enterTermo(self, ctx:BigTParser.TermoContext):
        pass

    # Exit a parse tree produced by BigTParser#termo.
    def exitTermo(self, ctx:BigTParser.TermoContext):
        pass


    # Enter a parse tree produced by BigTParser#MUL.
    def enterMUL(self, ctx:BigTParser.MULContext):
        pass

    # Exit a parse tree produced by BigTParser#MUL.
    def exitMUL(self, ctx:BigTParser.MULContext):
        pass


    # Enter a parse tree produced by BigTParser#DIV.
    def enterDIV(self, ctx:BigTParser.DIVContext):
        pass

    # Exit a parse tree produced by BigTParser#DIV.
    def exitDIV(self, ctx:BigTParser.DIVContext):
        pass


    # Enter a parse tree produced by BigTParser#DIGIT.
    def enterDIGIT(self, ctx:BigTParser.DIGITContext):
        pass

    # Exit a parse tree produced by BigTParser#DIGIT.
    def exitDIGIT(self, ctx:BigTParser.DIGITContext):
        pass


    # Enter a parse tree produced by BigTParser#ID.
    def enterID(self, ctx:BigTParser.IDContext):
        pass

    # Exit a parse tree produced by BigTParser#ID.
    def exitID(self, ctx:BigTParser.IDContext):
        pass


    # Enter a parse tree produced by BigTParser#ParenexprParen.
    def enterParenexprParen(self, ctx:BigTParser.ParenexprParenContext):
        pass

    # Exit a parse tree produced by BigTParser#ParenexprParen.
    def exitParenexprParen(self, ctx:BigTParser.ParenexprParenContext):
        pass


    # Enter a parse tree produced by BigTParser#c_chanel.
    def enterC_chanel(self, ctx:BigTParser.C_chanelContext):
        pass

    # Exit a parse tree produced by BigTParser#c_chanel.
    def exitC_chanel(self, ctx:BigTParser.C_chanelContext):
        pass



del BigTParser