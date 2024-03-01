%{
#include <iostream>
#include <math.h>
%}

delim [ \t\n]
brancos {delim}+
letra [A-Za-z]
digito [0-9]
id ({letra}({letra}|{digito}))
int [+-]?({digito}+)
double ({int}*\.{int}*)


%%
{brancos} ;
"("             return ABREP;
")"             return FECHAP;

if              return IF;
else            return ELSE;
while           return WHILE;
string          return STRING;
int             return INT;
double          return DOUBLE;
char            return CHAR;
bool            return BOOL;

{id}            return ID;
{num}           return NUM;
"="             return OP;
">="            return OP;
"<="            return OP;
"+"             return OP;
"-"             return OP;
"*"             return OP;
"/"             return OP;

%%

int main(int argc, char **argv){
    yyFlexLexer lexer;
    lexer.yylex();
}