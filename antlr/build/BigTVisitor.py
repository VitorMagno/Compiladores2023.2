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


    # Visit a parse tree produced by BigTParser#cmd_a.
    def visitCmd_a(self, ctx:BigTParser.Cmd_aContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BigTParser#cmd_na.
    def visitCmd_na(self, ctx:BigTParser.Cmd_naContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BigTParser#tipos_var.
    def visitTipos_var(self, ctx:BigTParser.Tipos_varContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BigTParser#atribuicao.
    def visitAtribuicao(self, ctx:BigTParser.AtribuicaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BigTParser#bool.
    def visitBool(self, ctx:BigTParser.BoolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BigTParser#mais_bool.
    def visitMais_bool(self, ctx:BigTParser.Mais_boolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BigTParser#expr.
    def visitExpr(self, ctx:BigTParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BigTParser#mais_expr.
    def visitMais_expr(self, ctx:BigTParser.Mais_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BigTParser#termo.
    def visitTermo(self, ctx:BigTParser.TermoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BigTParser#mais_termo.
    def visitMais_termo(self, ctx:BigTParser.Mais_termoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BigTParser#fator.
    def visitFator(self, ctx:BigTParser.FatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BigTParser#c_chanel.
    def visitC_chanel(self, ctx:BigTParser.C_chanelContext):
        return self.visitChildren(ctx)



del BigTParser