# Generated from BigT.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .BigTParser import BigTParser
else:
    from BigTParser import BigTParser

# This class defines a complete generic visitor for a parse tree produced by BigTParser.

class BigTVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by BigTParser#start.
    def visitStart(self, ctx:BigTParser.StartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BigTParser#programa_minipar.
    def visitPrograma_minipar(self, ctx:BigTParser.Programa_miniparContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BigTParser#bloco_stmt.
    def visitBloco_stmt(self, ctx:BigTParser.Bloco_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BigTParser#bloco_seq.
    def visitBloco_seq(self, ctx:BigTParser.Bloco_seqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BigTParser#bloco_par.
    def visitBloco_par(self, ctx:BigTParser.Bloco_parContext):  #thread
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BigTParser#chan.
    def visitChan(self, ctx:BigTParser.ChanContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BigTParser#prin.
    def visitPrin(self, ctx:BigTParser.PrinContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BigTParser#funcao.
    def visitFuncao(self, ctx:BigTParser.FuncaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BigTParser#atribuicao.
    def visitAtribuicao(self, ctx:BigTParser.AtribuicaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BigTParser#atr.
    def visitAtr(self, ctx:BigTParser.AtrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BigTParser#comp.
    def visitComp(self, ctx:BigTParser.CompContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BigTParser#rep.
    def visitRep(self, ctx:BigTParser.RepContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BigTParser#func.
    def visitFunc(self, ctx:BigTParser.FuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BigTParser#args.
    def visitArgs(self, ctx:BigTParser.ArgsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BigTParser#comparacao.
    def visitComparacao(self, ctx:BigTParser.ComparacaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BigTParser#comparacao_comp.
    def visitComparacao_comp(self, ctx:BigTParser.Comparacao_compContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BigTParser#repeticao.
    def visitRepeticao(self, ctx:BigTParser.RepeticaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BigTParser#DIV.
    def visitDIV(self, ctx:BigTParser.DIVContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BigTParser#ADD.
    def visitADD(self, ctx:BigTParser.ADDContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BigTParser#SUB.
    def visitSUB(self, ctx:BigTParser.SUBContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BigTParser#MUL.
    def visitMUL(self, ctx:BigTParser.MULContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BigTParser#simpleAtr2.
    def visitSimpleAtr2(self, ctx:BigTParser.SimpleAtr2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BigTParser#ParenexprParen.
    def visitParenexprParen(self, ctx:BigTParser.ParenexprParenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BigTParser#comparador.
    def visitComparador(self, ctx:BigTParser.ComparadorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BigTParser#GT.
    def visitGT(self, ctx:BigTParser.GTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BigTParser#LT.
    def visitLT(self, ctx:BigTParser.LTContext):
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


    # Visit a parse tree produced by BigTParser#comparador_rep.
    def visitComparador_rep(self, ctx:BigTParser.Comparador_repContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BigTParser#fator.
    def visitFator(self, ctx:BigTParser.FatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BigTParser#int.
    def visitInt(self, ctx:BigTParser.IntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BigTParser#id.
    def visitId(self, ctx:BigTParser.IdContext):
        return self.visitChildren(ctx)



del BigTParser