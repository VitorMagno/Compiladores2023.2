# Generated from BigT.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .BigTParser import BigTParser
else:
    from BigTParser import BigTParser

# This class defines a complete generic visitor for a parse tree produced by BigTParser.

class BigTVisitor(ParseTreeVisitor):

    def __init__(self):
        self.variables = {}

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
    def visitBloco_par(self, ctx:BigTParser.Bloco_parContext): #montar uma thread para rodar esse retorno
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BigTParser#chan.
    def visitChan(self, ctx:BigTParser.ChanContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BigTParser#prin.
    def visitPrin(self, ctx:BigTParser.PrinContext):
        name = self.visit(ctx.id())
        if(name not in self.variables):
            print("variavel nao declarada")
        else:
            print(self.variables[name])
        return 


    # Visit a parse tree produced by BigTParser#funcao.
    def visitFuncao(self, ctx:BigTParser.FuncaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BigTParser#atribuicao.
    def visitAtribuicao(self, ctx:BigTParser.AtribuicaoContext):
        variavel = self.visit(ctx.id_())
        valor
        if(ctx.expr() != None):
            valor = self.visit(ctx.expr())
        else:
            valor = self.visit(ctx.comparador())
        return 


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
        right = int(ctx.right().getText())
        left = int(ctx.left().getText())
        if(left != 0):
            return left/right
        else:
            print("divisao por 0")
        return


    # Visit a parse tree produced by BigTParser#ADD.
    def visitADD(self, ctx:BigTParser.ADDContext):
        right = int(ctx.right().getText())
        left = int(ctx.left().getText())
        return right+left


    # Visit a parse tree produced by BigTParser#SUB.
    def visitSUB(self, ctx:BigTParser.SUBContext):
        right = int(ctx.right().getText())
        left = int(ctx.left().getText())
        return right-left


    # Visit a parse tree produced by BigTParser#MUL.
    def visitMUL(self, ctx:BigTParser.MULContext):
        right = int(ctx.right().getText())
        left = int(ctx.left().getText())
        return right*left


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
        value = ctx.getText()
        return value


    # Visit a parse tree produced by BigTParser#id.
    def visitId(self, ctx:BigTParser.IdContext):
        name = ctx.getText()
        return name



del BigTParser