grammar BigT;		

progama_minipar:	bloco_stmt EOF
                ;
bloco_stmt:     bloco_seq 
        |       bloco_par
        ;
bloco_seq:      SEQ stmts;
bloco_par:      PAR stmts;
stmts:          atribuicao 
    |           stmt
    ;
stmt:           cmd_a 
    |           cmd_na
    ;
cmd_a:          IF '(' bool ')' cmd_a ELSE cmd_a 
    |           WHILE '(' bool ')' stmt
    ;
cmd_na:         IF '(' bool ')' stmt 
    |           IF '(' bool ')' cmd_a ELSE cmd_na
    ;    
tipos_var:      INT 
        |       CHAR
        ;
atribuicao:     id = expr;
bool:           termo mais_bool;
mais_bool:      (GE|LE|EQ|LT|GT|) termo mais_bool
        |
        ;
expr:           termo mais_expr;
mais_expr:      (ADD|SUB) termo mais_expr
        |
        ;
termo:          fator mais_termo;
mais_termo:     (MUL|DIV) fator mais_termo
          |
          ;
fator:          DIGIT | '(' expr ')';
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
ID  :   [a-zA-Z]+([0-9]*|[a-zA-Z]*);
CHAR:   [a-zA-Z];
DIGIT: ID;
CHAN: ID;
ID_COMP1: ID;
ID_COMP2: ID;
NEWLINE: '\r'? '\n' ;
SEQ :   'SEQ';
PAR :   'PAR';
INT :   [0-9]+ ;             // Define token INT as one or more digits
WS  :   [ \t]+ -> skip ;    // Define whitespace rule, toss it out