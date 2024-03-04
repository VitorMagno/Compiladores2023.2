%{
#include <iostream>
#include "sintatic.tab.h"
using namespace std;
    /* LT, LE, EQ, NE, GT, GE, IF, ELSE, WHILE, STRING, INT, DOUBLE, CHAR, ID, RELOP */
%}

%option noyywrap
delim [ \t\n]
brancos {delim}+
letra [A-Za-z]
digito [0-9]
id {letra}({letra}|{digito})*
int [+-]?({digito}+)
double ({int}+\.{int}+)
num {int}|{double}

%%
{brancos}       ;
[()]            {return YYText();}
if              {return (IF);}
else            {return (ELSE);}
while           {return (WHILE);}
string          {return (STRING);}
int             {return (INT);}
double          {return (DOUBLE);}
char            {return (CHAR);}
bool            {return (BOOL);}
{num}           {yyval.label = YYText(); return (NUM);}
{id}            {yyval.label = YYText(); return (ID);}
"=="            {yyval.label = YYText(); return (RELOP);}
"!="            {yyval.label = YYText(); return (RELOP);}
">"             {yyval.label = YYText(); return (RELOP);}
">="            {yyval.label = YYText(); return (RELOP);}
"<"             {yyval.label = YYText(); return (RELOP);}
"<="            {yyval.label = YYText(); return (RELOP);}
.               cout << YYText() << "Token invalido!\n";
%%

inserir_id(){

}

inserir_num(){

}