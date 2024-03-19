# Generated from BigT.g4 by ANTLR 4.13.1
from curses.ascii import isalpha
import multiprocessing
import subprocess
from antlr4 import *
from pyparsing import alphas
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
        result = multiprocessing.Process(self.visitChildren(ctx))
        result.start()
        result.join()
        return result

    # Visit a parse tree produced by BigTParser#chan.
    async def visitChan(self, ctx:BigTParser.ChanContext):
        a = await subprocess.Popen(['return self.visitChildren(ctx)'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        resultado = a.communicate()
        print(resultado)

    # Visit a parse tree produced by BigTParser#prin.
    def visitPrin(self, ctx:BigTParser.PrinContext):
        name = self.visit(ctx.id_())
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
        if(ctx.expr() != None):
            self.variables[variavel] = self.visit(ctx.expr())
        else:
            self.variables[variavel] = self.visit(ctx.comparador())
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


    # Visit a parse tree produced by BigTParser#comparacao.
    def visitComparacao(self, ctx:BigTParser.ComparacaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BigTParser#comparacao_comp.
    def visitComparacao_comp(self, ctx:BigTParser.Comparacao_compContext):
        boleano = self.visit(ctx.comparador())
        if(boleano == True):
            return self.visitChildren(ctx.stmts())
        else:
            return 


    # Visit a parse tree produced by BigTParser#repeticao.
    def visitRepeticao(self, ctx:BigTParser.RepeticaoContext):
        boleano = self.visit(ctx.comparador())
        if(boleano):
            while True:
                self.visit(ctx.stmts())
                if(self.visit(ctx.comparador()) == True):
                    continue
                else:
                    break
        return 


    # Visit a parse tree produced by BigTParser#DIV.
    def visitDIV(self, ctx:BigTParser.DIVContext):
        right = self.visit(ctx.right)
        left = self.visit(ctx.left)
        if(isalpha(right)):
            if(right in self.variables):
                right = int(self.variables.get(right))
            else:
                print("variavel nao declarada")
        if(isalpha(left)):
            if(left in self.variables):
                left = int(self.variables.get(left))
            else:
                print("variavel nao declarada")
        if(left != 0):
            return left / right
        else:
            print("divisao por 0")
        return

    # Visit a parse tree produced by BigTParser#ADD.
    def visitADD(self, ctx:BigTParser.ADDContext):
        right = self.visit(ctx.right)
        left = self.visit(ctx.left)
        if(isalpha(right)):
            if(right in self.variables):
                right = int(self.variables.get(right))
            else:
                print("variavel nao declarada")
        if(isalpha(left)):
            if(left in self.variables):
                left = int(self.variables.get(left))
            else:
                print("variavel nao declarada")
        return right + left


    # Visit a parse tree produced by BigTParser#SUB.
    def visitSUB(self, ctx:BigTParser.SUBContext):
        right = self.visit(ctx.right)
        left = self.visit(ctx.left)
        if(isalpha(right)):
            if(right in self.variables):
                right = int(self.variables.get(right))
            else:
                print("variavel nao declarada")
        if(isalpha(left)):
            if(left in self.variables):
                left = int(self.variables.get(left))
            else:
                print("variavel nao declarada")
        return left - right


    # Visit a parse tree produced by BigTParser#MUL.
    def visitMUL(self, ctx:BigTParser.MULContext):
        right = self.visit(ctx.right)
        left = self.visit(ctx.left)
        if(isalpha(right)):
            if(right in self.variables):
                right = int(self.variables.get(right))
            else:
                print("variavel nao declarada")
        if(isalpha(left)):
            if(left in self.variables):
                left = int(self.variables.get(left))
            else:
                print("variavel nao declarada")
        return right * left


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
        right = self.visit(ctx.right)
        left = self.visit(ctx.left)
        if(isalpha(right)):
            if(right in self.variables):
                right = int(self.variables.get(right))
            else:
                print("variavel nao declarada")
        if(isalpha(left)):
            if(left in self.variables):
                left = int(self.variables.get(left))
            else:
                print("variavel nao declarada")
        if(left > right):
            return True
        return False


    # Visit a parse tree produced by BigTParser#LT.
    def visitLT(self, ctx:BigTParser.LTContext):
        right = self.visit(ctx.right)
        left = self.visit(ctx.left)
        if(isalpha(right)):
            if(right in self.variables):
                right = int(self.variables.get(right))
            else:
                print("variavel nao declarada")
        if(isalpha(left)):
            if(left in self.variables):
                left = int(self.variables.get(left))
            else:
                print("variavel nao declarada")
        if(left < right):
            return True
        return False


    # Visit a parse tree produced by BigTParser#GE.
    def visitGE(self, ctx:BigTParser.GEContext):
        right = self.visit(ctx.right)
        left = self.visit(ctx.left)
        if(isalpha(right)):
            if(right in self.variables):
                right = int(self.variables.get(right))
            else:
                print("variavel nao declarada")
        if(isalpha(left)):
            if(left in self.variables):
                left = int(self.variables.get(left))
            else:
                print("variavel nao declarada")
        if(left >= right):
            return True
        return False


    # Visit a parse tree produced by BigTParser#LE.
    def visitLE(self, ctx:BigTParser.LEContext):
        right = self.visit(ctx.right)
        left = self.visit(ctx.left)
        if(isalpha(right)):
            if(right in self.variables):
                right = int(self.variables.get(right))
            else:
                print("variavel nao declarada")
        if(isalpha(left)):
            if(left in self.variables):
                left = int(self.variables.get(left))
            else:
                print("variavel nao declarada")
        if(left <= right):
            return True
        return False


    # Visit a parse tree produced by BigTParser#EQ.
    def visitEQ(self, ctx:BigTParser.EQContext):
        right = self.visit(ctx.right)
        left = self.visit(ctx.left)
        if(isalpha(right)):
            if(right in self.variables):
                right = int(self.variables.get(right))
            else:
                print("variavel nao declarada")
        if(isalpha(left)):
            if(left in self.variables):
                left = int(self.variables.get(left))
            else:
                print("variavel nao declarada")
        if(left == right):
            return True
        return False


    # Visit a parse tree produced by BigTParser#comparador_rep.
    def visitComparador_rep(self, ctx:BigTParser.Comparador_repContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BigTParser#fator.
    def visitFator(self, ctx:BigTParser.FatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BigTParser#int.
    def visitInt(self, ctx:BigTParser.IntContext):
        value = ctx.INTEGER().getText()
        return value


    # Visit a parse tree produced by BigTParser#id.
    def visitId(self, ctx:BigTParser.IdContext):
        name = ctx.ID().getText()
        return name



del BigTParser