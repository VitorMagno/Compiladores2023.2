%{
#include <stdio.h>
#include "sint.tab.h"
%}

%option noyywrap
%option yylineno

delim [ \t\n]
brancos {delim}+
letra [A-Za-z_]
digito [0-9]
id {letra}({letra}|{digito})*
int [+-]?({digito}+)

%%

{brancos}       ;
[()]            {return *yytext;}
if              {return (IF);}
else            {return (ELSE);}
while           {return (WHILE);}
{int}           {yylval.inteiro = atoi(yytext); return (INT);}
{id}            {yylval.id = *yytext; return (ID);}
"=="            {return EQ;}
"!="            {return NE;}
">="            {return GE;}
"<="            {return LE;}
">"             {return *yytext;}
"<"             {return *yytext;}
.               printf("Token %d invalido", *yytext);

%%