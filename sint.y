%{
#include <iostream>
#include <string>
#include <sstream>

#define YYSTYPE atributos

using namespace std;

struct atributos{
    string label;
    string traducao;
};

int yylex(void);
void yyerror(string);

%}

%token
%token
%token
%token

%start

%%


%%

#include "lex.yy.cpp"

int yyparse();