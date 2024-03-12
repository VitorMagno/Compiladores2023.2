# Generated from BigT.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .BigTParser import BigTParser
else:
    from BigTParser import BigTParser

# This class defines a complete generic visitor for a parse tree produced by BigTParser.

class BigTVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by BigTParser#progama_minipar.
    def visitProgama_minipar(self, ctx:BigTParser.Progama_miniparContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BigTParser#bloco_stmt.
    def visitBloco_stmt(self, ctx:BigTParser.Bloco_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BigTParser#bloco_seq.
    def visitBloco_seq(self, ctx:BigTParser.Bloco_seqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BigTParser#bloco_par.
    def visitBloco_par(self, ctx:BigTParser.Bloco_parContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BigTParser#stmts.
    def visitStmts(self, ctx:BigTParser.StmtsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BigTParser#stmt.
    def visitStmt(self, ctx:BigTParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BigTParser#IFelse.
    def visitIFelse(self, ctx:BigTParser.IFelseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BigTParser#WHILE.
    def visitWHILE(self, ctx:BigTParser.WHILEContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BigTParser#IF.
    def visitIF(self, ctx:BigTParser.IFContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BigTParser#IFelsena.
    def visitIFelsena(self, ctx:BigTParser.IFelsenaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BigTParser#INT.
    def visitINT(self, ctx:BigTParser.INTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BigTParser#CHAR.
    def visitCHAR(self, ctx:BigTParser.CHARContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BigTParser#atribuicao.
    def visitAtribuicao(self, ctx:BigTParser.AtribuicaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BigTParser#bool.
    def visitBool(self, ctx:BigTParser.BoolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BigTParser#GE.
    def visitGE(self, ctx:BigTParser.GEContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BigTParser#LE.
    def visitLE(self, ctx:BigTParser.LEContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BigTParser#EQ.
    def visitEQ(self, ctx:BigTParser.EQContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BigTParser#LT.
    def visitLT(self, ctx:BigTParser.LTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BigTParser#GT.
    def visitGT(self, ctx:BigTParser.GTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BigTParser#expr.
    def visitExpr(self, ctx:BigTParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BigTParser#ADD.
    def visitADD(self, ctx:BigTParser.ADDContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BigTParser#SUB.
    def visitSUB(self, ctx:BigTParser.SUBContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BigTParser#termo.
    def visitTermo(self, ctx:BigTParser.TermoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BigTParser#MUL.
    def visitMUL(self, ctx:BigTParser.MULContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BigTParser#DIV.
    def visitDIV(self, ctx:BigTParser.DIVContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BigTParser#DIGIT.
    def visitDIGIT(self, ctx:BigTParser.DIGITContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BigTParser#ID.
    def visitID(self, ctx:BigTParser.IDContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BigTParser#ParenexprParen.
    def visitParenexprParen(self, ctx:BigTParser.ParenexprParenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BigTParser#c_chanel.
    def visitC_chanel(self, ctx:BigTParser.C_chanelContext):
        return self.visitChildren(ctx)



del BigTParser