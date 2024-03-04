%{
#include <iostream>
#include <string>
#include <sstream>
#include <cctype>

#define YYSTYPE atributos

using namespace std;

struct atributos{
    string label;
    string traducao;
};

int yyparse(void);
int yylex(void);
void yyerror(const char *);

%}

%token DIGIT
%token SEQ
%token PAR


%start programa_minipar

%%
programa_minipar:   bloco_stmt          {;}
                ;
bloco_stmt:         bloco_seq           {;}
          |         bloco_par           {;}
          ;
bloco_seq:          SEQ stmts           {;}
         ;
bloco_par:          PAR stmts           {;}
         ;
tipos_var:          STRING              {;}
         |          INT                 {;}
         |          FLOAT               {;}
         |          BOOL                {;}
         |          CHAR                {;}
         ;
atribuicao:         id '=' expr         {;}
         ;
expr:               termo mais_expr     {;}
    ;
mais_expr:   '+' termo mais_expr        {;}
         |   '-' termo mais_expr        {;}
         |
         ;
termo:   fator mais_termo               {;}
     ;
mais_termo:   '*' fator mais_termo      {;}
          |   '/' fator mais_termo      {;}
          |
          ;
fator:   DIGIT               {;}
     | '(' expr ')'          {;}
     ;
c_chanel:
stmts:
cmd_a:
cmd_na:


%%

#include "lex.yy.cpp"

int yyparse();