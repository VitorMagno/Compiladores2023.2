%{
#include <iostream>
#include <cctype>
#include <map>
#include <cstdlib>
using namespace std;

int yylex(void);
int yyparse(void);
void yyerror(const char *);

map<string, double> variables;

bool evaluate_bool(double value) {
    return value != 0;
}

bool evaluate_bool(int value) {
    return value != 0;
}

bool evaluate_bool(bool value) {
    return value;
}

double get_value(string var_name) {
    if (variables.find(var_name) != variables.end())
        return variables[var_name];
    else {
        yyerror(("Variável '" + var_name + "' não definida.").c_str());
        return 0.0;
    }
}

void set_value(string var_name, double value) {
    variables[var_name] = value;
}
%}

%union {
    std::string palavra;
    int inteiro;
    float flutuante;
    char id[30];
    bool boolean;
    char caracter;
}

%token SEQ PAR IF ELSE WHILE GE LE NE EQ AND OR NOT
%token <id> ID
%token <id> ID_COMP1
%token <id> ID_COMP2
%token <id> CHAN
/* %token <inteiro> INTDIGIT */
%token <flutuante> FLOATDIGIT
/* %token <palavra> STRINGDIGIT */
/* %token <caracter> CHARDIGIT */
%token <inteiro> INT
%token <flutuante> FLOAT
%token <palavra> STRING
%token <boolean> TRUE FALSE
%token <caracter> CHAR
%token <boolean> BOOL

%start programa_minipar

%type <inteiro> bloco_seq bloco_par cmd_a cmd_na tipos_var expr fator atribuicao bool stmts
%type <palavra> programa_minipar

%left '+''-'
%left '*''/'
%left EQ NE '>' '<' GE LE
%left AND
%left OR
%right NOT

%%
programa_minipar: bloco_stmt    {cout << $1 << '\n';}
                ;
bloco_stmt: bloco_seq           {;}
          | bloco_par           {;}
          ;
bloco_seq: SEQ stmts            {$$=$2;}
         ;
bloco_par: PAR stmts            {;} /*falta*/
         ;
tipos_var: STRING               {if(typeof($2) != $1) yyerror("erro de tipo"); else $$ = $1;}
         | INT                  {if(typeof($2) != $1) yyerror("erro de tipo"); else $$ = $1;}
         | FLOAT                {if(typeof($2) != $1) yyerror("erro de tipo"); else $$ = $1;}
         | BOOL                 {if(typeof($2) != $1) yyerror("erro de tipo"); else $$ = $1;}
         | CHAR                 {if(typeof($2) != $1) yyerror("erro de tipo"); else $$ = $1;}
         ;
c_chanel: CHAN ID ID_COMP1 ID_COMP2 {;}; /*falta*/
stmts: atribuicao                   {set_value($1, $3); $$ = $3;}
     | stmt                         {;}
     ;
stmt: cmd_a                         {;}
    | cmd_na                        {;}
    ;
cmd_a: IF '(' bool ')' cmd_a ELSE cmd_a     {if($3) $$=$5; else $$=$$;} 
     | WHILE '(' bool ')' stmt              {while($3) $$=$5;} 
     ;
cmd_na: IF '(' bool ')' stmt                {if($3) $$=$5 ;} 
      | IF '(' bool ')' cmd_a ELSE cmd_na   {if($3) $$=$5 else{$$=$$};} 
      ;
bool:  expr EQ expr                         { $$ = ($1 == $3); }
       | expr NE expr                       { $$ = ($1 != $3); }
       | expr '>' expr                      { $$ = ($1 > $3); }
       | expr '<' expr                      { $$ = ($1 < $3); }
       | expr GE expr                       { $$ = ($1 >= $3); }
       | expr LE expr                       { $$ = ($1 <= $3); }
       | bool AND bool                      { $$ = ($1 && $3); }
       | bool OR bool                       { $$ = ($1 || $3); }
       | NOT bool                           { $$ = !($2); }
       | TRUE                               { $$ = true; }
       | FALSE                              { $$ = false; }
atribuicao: tipos_var ID '=' expr           {set_value($2, $3); $$ = $3}
          ;
expr: fator
    | ID                                    {$$ = get_value($1);}
    | expr '+' expr                         {$$ = $1 + $3;}
    | expr '-' expr                         {$$ = $1 + $3;}
    | expr '/' expr                         {$$ = $1 / $3;}
    | expr '*' expr                         {$$ = $1 * $3;}
    ;
fator: FLOATDIGIT                            {$$ = $1;}
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