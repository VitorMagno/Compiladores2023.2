all: bigT

bigT:	lex.yy.c bigT.tab.c 
	g++ lex.yy.c bigT.tab.c -std=c++17 -o bigT

lex.yy.c:	lex.l
	flex lex.l

bigT.tab.c:	sint.y
	bison -d sint.y

clean:
	rm bigT lex.yy.c bigT.tab.c bigT.tab.h