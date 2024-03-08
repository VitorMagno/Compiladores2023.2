%{
#include <iostream>
#include "sint.tab.h"
%}

%option noyywrap
%option yylineno

delim [ \t\n]
brancos {delim}+
letra [A-Za-z_]
digito [0-9]
string [{letra}+{digito}*]
id {letra}({letra}|{digito})*
int [+-]?({digito}+)
float ({int}+\.{int}+)
bool ["true"|"false"]

%%

{brancos}       ;
[()]            {return yytext;}
if              {return (IF);}
else            {return (ELSE);}
while           {return (WHILE);}
{string}        {yylval.palavra = yytext; return (STRING);}
{int}           {yylval.inteiro = atoi(yytext); return (INT);}
{float}         {yylval.flutuante = atof(yytext); return (FLOAT);}
{letra}         {yylval.letra = yytext; return (CHAR);}
{bool}          {yylval.boolean = yytext; return (BOOL);}
{id}            {strcopy(yylval.id, yytext); return (ID);}
"=="            {return EQ;}
"!="            {return NE;}
">="            {return GE;}
"<="            {return LE;}
">"             {yylval = yytext;}
"<"             {yylval = yytext;}
.               cout << yytext << "Token invalido!\n";

%%