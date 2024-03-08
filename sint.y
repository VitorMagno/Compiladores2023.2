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
};

%token SEQ PAR IF ELSE WHILE GE LE NE EQ AND OR NOT
%token <id> ID
%token <id> ID_COMP1
%token <id> ID_COMP2
%token <id> CHAN 
%token <inteiro> INTDIGIT
%token <flutuante> FLOATDIGIT
%token <palavra> STRINGDIGIT
%token <inteiro> INT
%token <flutuante> FLOAT
%token <palavra> STRING
%token <boolean> TRUE FALSE
%token <caracter> CHAR
%token <boolean> BOOL

%start programa_minipar
%type <id> c_chanel
%type <caracter> tipos_varChar 
%type <boolean> tipos_varBool atribuicaoBool fatorBool exprBool bool stmtsBool
%type <flutuante> tipos_varFloat atribuicaoFloat fatorFloat exprFloat cmd_a cmd_na stmt stmtsFloat bloco_seqFloat bloco_parFloat
%type <inteiro> tipos_varInt exprInt fatorInt atribuicaoInt 
%type <palavra> programa_minipar tipos_varString atribuicaoString fatorString exprString stmtsString bloco_stmt bloco_seqString bloco_parString

%left '+''-'
%left '*''/'
%left EQ NE '>' '<' GE LE
%left AND
%left OR
%right NOT

%%
programa_minipar: bloco_stmt    {cout << $1 << '\n';}
                ;
bloco_stmt: bloco_seqFloat      {$$ = toString($1);}
          | bloco_seqString          
          | bloco_parFloat      {$$ = toString($1);}
          | bloco_parString
          ;
bloco_seqFloat: SEQ stmtsFloat            {$$=$2;}
              ;
bloco_seqString: SEQ stmtsString           {$$=$2;}
         | SEQ stmtsBool             {$$=$2;}   
         ;
bloco_parFloat: PAR stmtsFloat            {;} /*falta*/
            ;
bloco_parString:PAR stmtsString           {;}
         | PAR stmtsBool             {;}
         ;
tipos_varString: STRING               {$$=$1}
               ;
tipos_varInt: INT                  {$$=$1}
            ;
tipos_varFloat: FLOAT                {$$=$1}
              ;
tipos_varBool: BOOL                 {$$=$1}
             ;
tipos_varChar: CHAR                 {$$=$1}
             ;
c_chanel: CHAN ID ID_COMP1 ID_COMP2 {;}; /*falta*/
stmtsFloat: atribuicaoInt                   {$$=$1;}
        | atribuicaoFloat                   {$$=$1;}
        | stmt        
stmtsString: atribuicaoString                   {$$=$1;}
            ;
stmtsBool: atribuicaoBool                   {$$=$1;}                       
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
bool:  exprInt EQ exprInt                         { if($1 == $3)$$ = true; else{$$ = false};}
       | exprInt NE exprInt                       { if($1 != $3)$$ = true; else{$$ = false} }
       | exprInt '>' exprInt                      { if($1 > $3)$$ = true; else{$$ = false}}
       | exprInt '<' exprInt                      {if($1 < $3)$$ = true; else{$$ = false}}
       | exprInt GE exprInt                       { if($1 >= $3)$$ = true; else{$$ = false}}
       | exprInt LE exprInt                       { if($1 <= $3)$$ = true; else{$$ = false} }
       | exprFloat EQ exprFloat                         { if($1 == $3)$$ = true; else{$$ = false};}
       | exprFloat NE exprFloat                       { if($1 != $3)$$ = true; else{$$ = false} }
       | exprFloat '>' exprFloat                      { if($1 > $3)$$ = true; else{$$ = false}}
       | exprFloat '<' exprFloat                      {if($1 < $3)$$ = true; else{$$ = false}}
       | exprFloat GE exprFloat                       { if($1 >= $3)$$ = true; else{$$ = false}}
       | exprFloat LE exprFloat                       { if($1 <= $3)$$ = true; else{$$ = false} }
       | bool AND bool                      {if($1 == false || $3 == false)$$ = false; else{$$ = true}}
       | bool OR bool                       {if($1 == true || $3 == true)$$ = true; else{$$ = false}}
       | NOT bool                           { if($2 == true)$$ = false; else{$$ = true}}
       | TRUE                               { $$ = true; }
       | FALSE                              { $$ = false; }
        ;
atribuicaoString: tipos_varString ID '=' exprString           {set_value($2, $4); $$ = $4}
          ;
atribuicaoInt: tipos_varInt ID '=' exprInt           {set_value($2, $4); $$ = $4}
          ;
atribuicaoFloat: tipos_varFloat ID '=' exprFloat           {set_value($2, $4); $$ = $4}
          ;
atribuicaoBool: tipos_varBool ID '=' exprBool           {set_value($2, $4); $$ = $4}
          ;
exprInt: fatorInt
    | ID                                    {$$ = get_value($1);}
    | exprInt '+' exprInt                         {$$ = $1 + $3;}
    | exprInt '-' exprInt                         {$$ = $1 + $3;}
    | exprInt '/' exprInt                         {$$ = $1 / $3;}
    | exprInt '*' exprInt                         {$$ = $1 * $3;}
    ;
exprFloat: fatorFloat
    | ID                                             {$$ = get_value($1);}
    | exprFloat '+' exprFloat                        {$$ = $1 + $3;}
    | exprFloat '-' exprFloat                         {$$ = $1 + $3;}
    | exprFloat '/' exprFloat                         {$$ = $1 / $3;}
    | exprFloat '*' exprFloat                         {$$ = $1 * $3;}
    ;
exprString: ID                                             {$$ = get_value($1);}
        | fatorString
        ;
exprBool: ID                                             {$$ = get_value($1);}
        | fatorBool
        ;
fatorFloat: FLOATDIGIT  {$$ = $1;}
     | '(' exprFloat ')'     {$$ = $2;}
     ;
fatorInt: INTDIGIT  {$$ = $1;}
     |'(' exprInt ')'     {$$ = $2;}
     ;
fatorString: STRINGDIGIT | CHAR {$$ = $1;}
    |'(' exprString ')'     {$$ = $2;}
     ;
fatorBool: BOOL {$$ = $1;}
        | '(' exprBool ')'     {$$ = $2;}
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