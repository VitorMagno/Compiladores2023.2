grammar BigT;		

progama_minipar:	bloco_stmt
            ;
bloco_stmt:     bloco_seq 
        |       bloco_par
        ;
bloco_seq:      'SEQ' stmts;
bloco_par:      'PAR' stmts;
stmts:          atribuicao 
    |           stmt
    ;
stmt:           cmd_a 
    |           cmd_na
    ;
cmd_a:          'IF' '(' bool ')' cmd_a 'ELSE' cmd_a  # IFelse
    |           'WHILE' '(' bool ')' stmt             # WHILE
    ;
cmd_na:         'IF' '(' bool ')' stmt                # IF
    |           'IF' '(' bool ')' cmd_a 'ELSE' cmd_na # IFelsena
    ;    
tipos_var:      INT                     # INT
        |       CHAR                    # CHAR
        ;
atribuicao:     ID '=' expr;           
bool:           termo mais_bool;
mais_bool:       GE termo mais_bool?     # GE
        |        LE termo mais_bool?     # LE
        |        EQ termo mais_bool?     # EQ
        |        LT termo mais_bool?     # LT
        |        GT termo mais_bool?     # GT
        ;
expr:           termo mais_expr;
mais_expr:      ADD termo mais_expr?    # ADD
        |       SUB termo mais_expr?     # SUB
        ;
termo:          fator mais_termo?;
mais_termo:     MUL fator mais_termo?    # MUL
          |     DIV fator mais_termo?    # DIV
          ;
fator:    DIGIT                         # DIGIT
    |      ID                           # ID
    | '(' expr ')'                      # ParenexprParen
    ;
c_chanel:       CHAN ID ID_COMP1 ID_COMP2;

// parser rules start with lowercase letters, lexer rules with uppercase
IF :   'IF';
ELSE :   'ELSE';
WHILE :   'WHILE';
AND :   '&&';
OR :   '||';
NOT:    '!';
GE :    '>=';
LE :    '<=';
EQ :    '==';
LT:     '<';
GT :    '>';
MUL :   '*' ;                   // assigns token name to '*' used above in grammar
DIV :   '/' ;
ADD :   '+' ;
SUB :   '-' ;
CHAR:   [a-zA-Z];
ID  :   CHAR+([0-9]*|[a-zA-Z]*);
DIGIT: CHAR+([0-9]*|[a-zA-Z]*)|INT;
CHAN: CHAR+([0-9]*|[a-zA-Z]*);
ID_COMP1: CHAR+([0-9]*|[a-zA-Z]*);
ID_COMP2: CHAR+([0-9]*|[a-zA-Z]*);
NEWLINE: '\r'? '\n' ;
SEQ :   'SEQ';
PAR :   'PAR';
INT :   [0-9]+ ;             // Define token INT as one or more digits
WS  :   [ \t]+ -> skip ;    // Define whitespace rule, toss it out