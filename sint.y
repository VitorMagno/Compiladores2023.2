%{
#include <iostream>
#include <cctype>
#include <unordered_map>
using std::string;
using std::cout;
using std::unordered_map;

int yylex(void);
int yyparse(void);
void yyerror(const char *);
unordered_map<string, float> variables;
%}
//tipo double para os atributos em yylval
%define api.value.type {float}

%union {
    string palavra;
    int inteiro;
    float flutuante;
    char id[30];
    bool boolean;
    char caracter;
}

%token SEQ PAR IF ELSE WHILE
%token <id> ID
%token <id> ID_COMP1
%token <id> ID_COMP2
%token <id> CHAN
%token <flutuante><inteiro> DIGIT
%token <inteiro> INT
%token <flutuante> DOUBLE
%token <palavra> STRING
%token <boolean> BOOL
%token <caracter> CHAR

%start programa_minipar

%type 

%%
programa_minipar: bloco_stmt    {;}
                ;
bloco_stmt: bloco_seq           {;}
          | bloco_par           {;}
          ;
bloco_seq: SEQ stmts            {;}
         ;
bloco_par: PAR stmts            {;}
         ;
tipos_var: STRING               {;}
         | INT                  {;}
         | DOUBLE                {;}
         | BOOL                 {;}
         | CHAR                 {;}
         ;
c_chanel: CHAN ID ID_COMP1 ID_COMP2 {;}; /*falta*/
stmts: atribuicao                   {;}
     | stmt                         {;}
     ;
stmt: cmd_a                         {;}
    | cmd_na                        {;}
    ;
cmd_a: IF '(' BOOL ')' cmd_a ELSE cmd_a     {;} /*falta*/
     | WHILE '(' BOOL ')' stmt              {;} /*falta*/
     ;
cmd_na: IF '(' bool ')' stmt                {;} /*falta*/
      | IF '(' bool ')' cmd_a ELSE cmd_na   {;} /*falta*/
      ;
bool: ID '=''=' ID                          {;} /*falta*/
    | ID '!''=' ID                          {;} /*falta*/
    | ID '>' ID                             {;} /*falta*/
    | ID '>''=' ID                          {;} /*falta*/
    | ID '<' ID                             {;} /*falta*/
    | ID '<''=' ID                          {;} /*falta*/
    ;
atribuicao: ID '=' expr                     {variables[$1] = $3;}
         ;
expr: termo mais_expr                       {$$ = $1;}
    ;
mais_expr: '+' termo mais_expr              {$$ = $$ + $2;}
         | '-' termo mais_expr              {$$ = $$ - $2;}
         |
         ;
termo:   fator mais_termo                   {$$ = $1;}
     ;
mais_termo: '*' fator mais_termo            {$$ = $$ * $2;}
          | '/' fator mais_termo    
          {if($2==0){
            yyerror("divisao por zero")
          }else{
            $$ = $$ / $2
          };}
          |
          ;
fator: DIGIT                        
     {if(variables.find($1) != unordered_map::end){
         $$ = variables[$1]
     }else{
         yyerror("variavel nao declarada")
     };}
     | '(' expr ')'                         {$$ = $2;}
     ;
%%

#include "lex.yy.c"

int main(){
    yy.parse();
}

void yyerror(const char * s){
    extern int yylineno;
    extern char *yytext;

    cout<<"ERRO: "<<s<<" secao \"" << yytext << "\" linha "<< yylineno <<'\n';
}