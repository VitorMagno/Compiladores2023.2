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
    int inteiro;
    float flutuante;
    char id[26];
    bool booleano;
    string palavra;
};

%token SEQ PAR IF ELSE WHILE GE LE NE EQ AND OR NOT TRUE FALSE
%token <id> ID
%token <id> ID_COMP1
%token <id> ID_COMP2
%token <id> CHAN 
%token <inteiro> INTDIGIT

%start programa_minipar
%type <id> c_chanel
%type <inteiro> tipos_var expr fator atribuicao cmd_a cmd_na stmts bloco_seq bloco_par stmt
%type <booleano> bool
%type <palavra> bloco_stmt
%left '+''-'
%left '*''/'
%left EQ NE '>' '<' GE LE
%left AND
%left OR
%right NOT

%%
programa_minipar: bloco_stmt    {cout << $1 << '\n';}
                ;
bloco_stmt: bloco_seq      {$$ = toString($1);}          
          | bloco_par      {$$ = toString($1);}
          ;
bloco_seq: SEQ stmts            {$$=$2;}
        ;
bloco_par: PAR stmts            {;} /*falta*/
            ;
tipos_var: INTDIGIT                  {$$=$1}
        ;
c_chanel: CHAN ID ID_COMP1 ID_COMP2 {;}; /*falta*/
stmts: atribuicao                   {$$=$1;}
    | stmt
    ;        
stmt: cmd_a                         
    | cmd_na                        
    ;
cmd_a: IF '(' bool ')' cmd_a ELSE cmd_a     {if($3) $$=$5; else $$=$$;} 
     | WHILE '(' bool ')' stmt              {while($3) $$=$5;} 
     ;
cmd_na: IF '(' bool ')' stmt                {if($3) $$=$5 ;} 
      | IF '(' bool ')' cmd_a ELSE cmd_na   {if($3) $$=$5 else{$$=$$};} 
      ;
bool:  expr EQ expr                      { if($1 == $3)$$ = true; else{$$ = false};}
    |  expr NE expr                      { if($1 != $3)$$ = true; else{$$ = false} }
    |  expr '>' expr                     { if($1 > $3)$$ = true; else{$$ = false}}
    |  expr '<' expr                     {if($1 < $3)$$ = true; else{$$ = false}}
    |  expr GE expr                      { if($1 >= $3)$$ = true; else{$$ = false}}
    |  expr LE expr                      { if($1 <= $3)$$ = true; else{$$ = false} }
    | bool AND bool                      {if($1 == false || $3 == false)$$ = false; else{$$ = true}}
    | bool OR bool                       {if($1 == true || $3 == true)$$ = true; else{$$ = false}}
    | NOT bool                           { if($2 == true)$$ = false; else{$$ = true}}
    | TRUE                               { $$ = true; }
    | FALSE                              { $$ = false; }
    ;
atribuicao: tipos_var ID '=' expr           {set_value($2, $4); $$ = $4}
          ;
expr: fator
    | ID                                    {$$ = get_value($1);}
    | expr '+' expr                         {$$ = $1 + $3;}
    | expr '-' expr                         {$$ = $1 + $3;}
    | expr '/' expr                         {$$ = $1 / $3;}
    | expr '*' expr                         {$$ = $1 * $3;}
    ;

fator: INTDIGIT           {$$ = $1;}
     |'(' expr ')'     {$$ = $2;}
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