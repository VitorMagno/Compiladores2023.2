grammar BigT;

start: programa_minipar (EOF)
    ;
programa_minipar:	bloco_stmt
            ;
bloco_stmt:     bloco_seq
        |       bloco_par
        ;
bloco_seq:      'SEQ' (NEWLINE) (ENTRATAB) stmts+ (NEWLINE) (CONTRATAB);
bloco_par:      'PAR' (NEWLINE) (ENTRATAB) stmts+ (NEWLINE) (CONTRATAB);
stmts:          atribuicao 
    |           (NEWLINE)? stmt
    ;
stmt:           (NEWLINE)? cmd_a 
    |           (NEWLINE)? cmd_na
    ;
cmd_a:          'if' '(' bool ')' (NEWLINE)? (ENTRATAB)? cmd_a (NEWLINE)? (CONTRATAB)? 'else' (ENTRATAB)? cmd_a (NEWLINE)? (CONTRATAB)? # IFelse
    |           'while' '(' bool ')' (NEWLINE)? (ENTRATAB)? stmts (NEWLINE)? (CONTRATAB)?             # WHILE
    ;
cmd_na:         'if' '(' bool ')' (NEWLINE)? (ENTRATAB)? stmts (NEWLINE)? (CONTRATAB)?                # IF
    |           'if' '(' bool ')' (NEWLINE)? (ENTRATAB)? cmd_a (NEWLINE)? (CONTRATAB)? 'else' (NEWLINE)? (ENTRATAB)? cmd_na (NEWLINE)? (CONTRATAB)? # IFelsena
    ;    
tipos_var:      (NEWLINE)? INT                     # INT
        |       (NEWLINE)? CHAR                    # CHAR
        ;
atribuicao:     (ID) '=' expr (NEWLINE);           
bool:           termo mais_bool;
mais_bool:       (GE) termo mais_bool?     (NEWLINE)?# GE
        |        (LE) termo mais_bool?     (NEWLINE)?# LE
        |        (EQ) termo mais_bool?     (NEWLINE)?# EQ
        |        (LT) termo mais_bool?     (NEWLINE)?# LT
        |        (GT) termo mais_bool?     (NEWLINE)?# GT                
        ;
expr:           termo mais_expr;
mais_expr:      (ADD) termo mais_expr?     (NEWLINE)?# ADD
        |       (SUB) termo mais_expr?     (NEWLINE)?# SUB
        ;
termo:          fator mais_termo?;
mais_termo:     (MUL) fator mais_termo?    (NEWLINE)?# MUL
          |     (DIV) fator mais_termo?    (NEWLINE)?# DIV
          ;
fator:    (DIGIT)    (NEWLINE)?                     # DIGIT
    |      (ID)      (NEWLINE)?                     # ID
    | '(' expr ')' (NEWLINE)?                     # ParenexprParen
    ;
c_chanel:  'CHAN' {ID} 'id_comp1' 'id_comp2' (NEWLINE);

// parser rules start with lowercase letters, lexer rules with uppercase
AND :   '&&';
OR :    '||';
NOT:    '!';
GE :    '>=';
LE :    '<=';
EQ :    '==';
LT:     '<';
GT :    '>';
MUL :   '*';                   // assigns token name to '*' used above in grammar
DIV :   '/';
ADD :   '+';
SUB :   '-';
CHAR:   [a-zA-Z];
ID  :   [a-zA-Z]+;
INT :   [0-9]+ ;
DIGIT: CHAR+([0-9]*|[a-zA-Z]*)|INT;
CHAN: [CHAN];
ID_COMP1: CHAR+([0-9]*|[a-zA-Z]*);
ID_COMP2: CHAR+([0-9]*|[a-zA-Z]*);
NEWLINE: '\r'? '\n';
SEQ :   [SEQ];
PAR :   [PAR];
ENTRATAB:  [ \t]+;
CONTRATAB: [ \b];
SINGLE_SPACE: ' ';
WS  :   SINGLE_SPACE -> skip;    // Define whitespace rule, toss it out