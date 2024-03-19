# Generated from BigT.g4 by ANTLR 4.13.1
from ast import stmt
from antlr4 import *
from sympy import true
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
    def visitBloco_par(self, ctx:BigTParser.Bloco_parContext):  #thread
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BigTParser#chan.
    def visitChan(self, ctx:BigTParser.ChanContext): #sockets
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BigTParser#prin.
    def visitPrin(self, ctx:BigTParser.PrinContext):
        print(ctx.getToken)
        return


    # Visit a parse tree produced by BigTParser#funcao.
    def visitFuncao(self, ctx:BigTParser.FuncaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BigTParser#atribuicao.
    def visitAtribuicao(self, ctx:BigTParser.AtribuicaoContext):
        idatual = self.visitChildren(ctx.id_())
        if(self.visitChildren(ctx.expr()) != None):
            expratual=self.visitChildren(ctx.expr())
            if(idatual not in self.variables.keys()):
                self.variables[idatual] = expratual
        else:
            comparadoratual=self.visitChildren(ctx.comparador())
            if(comparadoratual not in self.variables.keys()):
                self.variables[idatual] = comparadoratual
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
        result = self.visitChildren(ctx.comparador())
        if(result == True):
            return self.visitChildren(ctx.stmts())
        return 



    # Visit a parse tree produced by BigTParser#repeticao.
    def visitRepeticao(self, ctx:BigTParser.RepeticaoContext):
        while(self.visitChildren(ctx.comparador()) == True):
            return self.visitChildren(ctx.stmts())
        return


    # Visit a parse tree produced by BigTParser#DIV.
    def visitDIV(self, ctx:BigTParser.DIVContext):
        left = ctx.expr(0)
        right = ctx.expr(1)
        if(right != 0):
            resultado = left/right
            return resultado
        else:
            print('divisao por 0')
            return


    # Visit a parse tree produced by BigTParser#ADD.
    def visitADD(self, ctx:BigTParser.ADDContext):
        left = self.visitChildren(ctx.expr(0))
        right = self.visitChildren(ctx.expr(1))
        resultado = left+right
        return resultado


    # Visit a parse tree produced by BigTParser#SUB.
    def visitSUB(self, ctx:BigTParser.SUBContext):
        left = self.visitChildren(ctx.expr(0))
        right = self.visitChildren(ctx.expr(1))
        resultado = left-right
        return resultado


    # Visit a parse tree produced by BigTParser#MUL.
    def visitMUL(self, ctx:BigTParser.MULContext):
        left = self.visitChildren(ctx.expr(0))
        right = self.visitChildren(ctx.expr(1))
        resultado = left*right
        return resultado


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
        left = self.visitChildren(ctx.expr(0))
        right = self.visitChildren(ctx.expr(1))
        if (left > right):
            return True
        return False


    # Visit a parse tree produced by BigTParser#LT.
    def visitLT(self, ctx:BigTParser.LTContext):
        left = self.visitChildren(ctx.expr(0))
        right = self.visitChildren(ctx.expr(1))
        if (left < right):
            return True
        return False


    # Visit a parse tree produced by BigTParser#GE.
    def visitGE(self, ctx:BigTParser.GEContext):
        left = self.visitChildren(ctx.expr(0))
        right = self.visitChildren(ctx.expr(1))
        if (left >= right):
            return True
        return False


    # Visit a parse tree produced by BigTParser#LE.
    def visitLE(self, ctx:BigTParser.LEContext):
        left = self.visitChildren(ctx.expr(0))
        right = self.visitChildren(ctx.expr(1))
        if (left <= right):
            return True
        return False


    # Visit a parse tree produced by BigTParser#EQ.
    def visitEQ(self, ctx:BigTParser.EQContext):
        left = self.visitChildren(ctx.expr(0))
        right = self.visitChildren(ctx.expr(1))
        if (left == right):
            return True
        return False


    # Visit a parse tree produced by BigTParser#comparador_rep.
    def visitComparador_rep(self, ctx:BigTParser.Comparador_repContext): #np
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BigTParser#fator.
    def visitFator(self, ctx:BigTParser.FatorContext):  #np
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BigTParser#int.
    def visitInt(self, ctx:BigTParser.IntContext):
        return int(ctx.getText())


    # Visit a parse tree produced by BigTParser#id.
    def visitId(self, ctx:BigTParser.IdContext):
        print(ctx.getText())
        return ctx.getText()



del BigTParser