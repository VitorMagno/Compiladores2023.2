all: lexic sintatic compi

lexic:
	flex lex.l

sintatic:
	bison -d sint.y

compi:
	g++ -o minipar sintatic.tab.cpp lex.yy.cpp -lfl