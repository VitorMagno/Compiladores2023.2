%{
#include <iostream>
#include "bigT.tab.h"
extern float variables[100];
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
[(|)]           {return yytext;}
if              {return (IF);}
else            {return (ELSE);}
while           {return (WHILE);}
{string}        {yylval.num = yytext; return (STRING);}
{int}           {yylval.num = atoi(yytext); return (INT);}
{float}         {yylval.num = atof(yytext); return (float);}
{letra}         {yylval.num = yytext; return (CHAR);}
{bool}          {yylval.num = yytext; return (BOOL);}
{id}            {strcopy(yylval.id, yytext); return (ID);}
"=="            {yylval = yytext; return (EQ);}
"!="            {yylval = yytext; return (NE);}
">"             {yylval = yytext; return (GT);}
">="            {yylval = yytext; return (GE);}
"<"             {yylval = yytext; return (LT);}
"<="            {yylval = yytext; return (LE);}
.               cout << yytext << "Token invalido!\n";

%%