%{
#include <iostream>
using std::cout;
%}

%option noyywrap
delim [ \t\n]
brancos {delim}+
letra [A-Za-z]
digito [0-9]
id {letra}({letra}|{digito})*
int [+-]?({digito}+)
double ({int}*\.{int}+)

%%
{brancos}       ;
[()]            return *yytext;
if              return IF;
else            return ELSE;
while           return WHILE;
string          return STRING;
int             return INT;
double          return DOUBLE;
char            return CHAR;
bool            return BOOL;
{num}           {yyval.label = yytext; return NUM;}
{id}            {yyval.label = yytext; return ID;}
"=="            return OP;
">="            return OP;
"<="            return OP;
.               cout << YYText() << "Token invalido!\n";
%%