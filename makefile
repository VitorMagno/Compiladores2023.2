all:	bigT

bigT:	lex.yy.c sint.tab.c 
	g++ lex.yy.c sint.tab.c -std=c++17 -o bigT

lex.yy.c:	lex.l
	flex lex.l

sint.tab.c:	sint.y
	bison -d sint.y

clean:
	rm bigT lex.yy.c sint.tab.c sint.tab.h