# Generated from BigT.g4 by ANTLR 4.13.1
from antlr4 import *
from black import nullcontext
if "." in __name__:
    from .BigTParser import BigTParser
else:
    from BigTParser import BigTParser

# This class defines a complete generic visitor for a parse tree produced by BigTParser.

class BigTVisitor(ParseTreeVisitor):

    def __init__(self):
        self.memory = {}

    # Visit a parse tree produced by BigTParser#progama_minipar.
    def visitPrograma_minipar(self, ctx:BigTParser.Programa_miniparContext):
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
        condicao = self.visit(ctx.bool())
        if(condicao):
            return self.visit(ctx.cmd_a())
        else:
            return self.visit(ctx.cmd_a())


    # Visit a parse tree produced by BigTParser#WHILE.
    def visitWHILE(self, ctx:BigTParser.WHILEContext):
        condicao = self.visit(ctx.bool())
        while(bool):
            return self.visit(ctx.stmt())


    # Visit a parse tree produced by BigTParser#IF.
    def visitIF(self, ctx:BigTParser.IFContext):
        condicao = self.visit(ctx.bool())
        if(condicao):
            return self.visit(ctx.cmd_a())


    # Visit a parse tree produced by BigTParser#IFelsena.
    def visitIFelsena(self, ctx:BigTParser.IFelsenaContext):
        condicao = self.visit(ctx.bool())
        if(condicao):
            return self.visit(ctx.cmd_a())
        else:
            return self.visit(ctx.cmd_na)


    # Visit a parse tree produced by BigTParser#INT.
    def visitINT(self, ctx:BigTParser.INTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BigTParser#CHAR.
    def visitCHAR(self, ctx:BigTParser.CHARContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BigTParser#atribuicao.
    def visitAtribuicao(self, ctx:BigTParser.AtribuicaoContext):
        name = ctx.ID().getText()
        value = self.visit(ctx.expr())
        self.memory[name] = value
        return value

    # Visit a parse tree produced by BigTParser#bool.
    def visitBool(self, ctx:BigTParser.BoolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BigTParser#GE.
    def visitGE(self, ctx:BigTParser.GEContext):
        termo1 = self.visitBool(ctx.termo())
        termo2 = self.visit(ctx.termo())
        if(termo1 >= termo2):
            return True
        else:
            return False


    # Visit a parse tree produced by BigTParser#LE.
    def visitLE(self, ctx:BigTParser.LEContext):
        termo1 = self.visitBool(ctx.termo())
        termo2 = self.visit(ctx.termo())
        if(termo1 <= termo2):
            return True
        else:
            return False


    # Visit a parse tree produced by BigTParser#EQ.
    def visitEQ(self, ctx:BigTParser.EQContext):
        termo1 = self.visitBool(ctx.termo())
        termo2 = self.visit(ctx.termo())
        if(termo1 == termo2):
            return True
        else:
            return False


    # Visit a parse tree produced by BigTParser#LT.
    def visitLT(self, ctx:BigTParser.LTContext):
        termo1 = self.visitBool(ctx.termo())
        termo2 = self.visit(ctx.termo())
        if(termo1 < termo2):
            return True
        else:
            return False


    # Visit a parse tree produced by BigTParser#GT.
    def visitGT(self, ctx:BigTParser.GTContext):
        termo1 = self.visitBool(ctx.termo())
        termo2 = self.visit(ctx.termo())
        if(termo1 > termo2):
            return True
        else:
            return False


    # Visit a parse tree produced by BigTParser#expr.
    def visitExpr(self, ctx:BigTParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BigTParser#ADD.
    def visitADD(self, ctx:BigTParser.ADDContext):
        termo1 = self.visitExpr(ctx.termo())
        termo2 = self.visit(ctx.termo())
        return termo1 + termo2


    # Visit a parse tree produced by BigTParser#SUB.
    def visitSUB(self, ctx:BigTParser.SUBContext):
        termo1 = self.visitExpr(ctx.termo())
        termo2 = self.visit(ctx.termo())
        return termo1 - termo2


    # Visit a parse tree produced by BigTParser#termo.
    def visitTermo(self, ctx:BigTParser.TermoContext):
        if (self.visit(ctx.mais_termo()) is not nullcontext):
            return self.visit(ctx.mais_termo())
        else:
            return self.visit(ctx.fator())


    # Visit a parse tree produced by BigTParser#MUL.
    def visitMUL(self, ctx:BigTParser.MULContext):
        termo1 = self.visitTermo(ctx.fator())
        termo2 = self.visit(ctx.fator())
        return termo1 * termo2


    # Visit a parse tree produced by BigTParser#DIV.
    def visitDIV(self, ctx:BigTParser.DIVContext):
        termo1 = self.visitTermo(ctx.fator())
        termo2 = self.visit(ctx.fator())        
        return termo1 / termo2


    # Visit a parse tree produced by BigTParser#DIGIT.
    def visitDIGIT(self, ctx:BigTParser.DIGITContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BigTParser#ID.
    def visitID(self, ctx:BigTParser.IDContext):
        name = ctx.ID().getText()
        if(self.visit(ctx) in self.memory):
            r = self.memory[name]
        if(type(r) is int):
            r = int(r)
        else:
            r = str(r)
        return r


    # Visit a parse tree produced by BigTParser#ParenexprParen.
    def visitParenexprParen(self, ctx:BigTParser.ParenexprParenContext):
        return self.visit(ctx.expr())


    # Visit a parse tree produced by BigTParser#c_chanel.
    def visitC_chanel(self, ctx:BigTParser.C_chanelContext):
        nome_conexao = self.visit(ctx.ID.getText())
        id_pc1 = self.visit(ctx.ID_COMP1.getText())
        id_pc2 = self.visit(ctx.ID_COMP2.getText())
        return 



del BigTParser