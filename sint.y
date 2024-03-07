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

%token SEQ PAR IF ELSE WHILE GE LE NE EQ
%token <id> ID
%token <id> ID_COMP1
%token <id> ID_COMP2
%token <id> CHAN
%token <inteiro> INTDIGIT
%token <flutuante> FLOATDIGIT
%token <palavra> STRINGDIGIT
%token <caracter> CHARDIGIT
%token <inteiro> INT
%token <flutuante> FLOAT
%token <palavra> STRING
%token <boolean> BOOL
%token <caracter> CHAR

%start programa_minipar

%type <inteiro> bloco_seq bloco_par cmd_a cmd_na tipos_var expr mais_expr termo mais_termo fator

%%
programa_minipar: bloco_stmt    {;}
                ;
bloco_stmt: bloco_seq           {;}
          | bloco_par           {;}
          ;
bloco_seq: SEQ stmts            {$$=$2;}
         ;
bloco_par: PAR stmts            {;} /*falta*/
         ;
tipos_var: STRING               {$$ = string;}
         | INT                  {$$ = int;}
         | FLOAT                {$$ = float;}
         | BOOL                 {$$ = bool;}
         | CHAR                 {$$ = char;}
         ;
c_chanel: CHAN ID ID_COMP1 ID_COMP2 {;}; /*falta*/
stmts: atribuicao                   {;}
     | stmt                         {;}
     ;
stmt: cmd_a                         {;}
    | cmd_na                        {;}
    ;
cmd_a: IF '(' bool ')' cmd_a ELSE cmd_a     {if($3){$$=$5}else{$$=$7};} 
     | WHILE '(' bool ')' stmt              {while($3){$$=$5};} 
     ;
cmd_na: IF '(' bool ')' stmt                {if($3){$$=$5};} 
      | IF '(' bool ')' cmd_a ELSE cmd_na   {if($3){$$=$5}else{$$=$7};} 
      ;
bool: expr
    ;
atribuicao: tipos_var ID '=' expr                     {variables[$1] = $3;}
         ;
expr: termo mais_expr                       {$$ = $1;}
    ;
mais_expr: '+' termo mais_expr              {$$ = $-1 + $2;}
         | '-' termo mais_expr              {$$ = $-1 - $2;}
         | GE termo mais_expr               {$$ = $-1 >= $2;}
         | LE termo mais_expr               {$$ = $-1 <= $2;}
         | NE termo mais_expr               {$$ = $-1 != $2;}
         | EQ termo mais_expr               {$$ = $-1 == $2;}
         | '>' termo mais_expr              {$$ = $-1 > $2;}
         | '<' termo mais_expr              {$$ = $-1 < $2;}
         |
         ;
termo:   fator mais_termo                   {$$ = $1;}
     ;
mais_termo: '*' fator mais_termo            {$$ = $-1 * $2;}
          | '/' fator mais_termo    
          {if($2==0){
            yyerror("divisao por zero")
          }else{
            $$ = $-1 / $2
          };}
          |
          ;
fator: INTDIGIT | FLOATDIGIT | CHARDIGIT | STRINGDIGIT                        
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

    cout << "ERRO: " << s << " secao \"" << yytext << "\" linha " << yylineno << '\n';
}