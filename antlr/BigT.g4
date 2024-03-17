grammar BigT;

start: programa_minipar
    ;
programa_minipar:	bloco_stmt
            ;
bloco_stmt:     bloco_seq
        |       bloco_par
        ;
bloco_seq:      NEWLINE*SINGLE_SPACE*ENTRATAB* 'SEQ' ((NEWLINE)(ENTRATAB)) stmts+ ENDLINE* CONTRATAB* EOF;
bloco_par:      NEWLINE*SINGLE_SPACE*ENTRATAB* 'PAR' ((NEWLINE)(ENTRATAB)) stmts+ ENDLINE* CONTRATAB* EOF;
stmts:          NEWLINE*SINGLE_SPACE*ENTRATAB* atribuicao   ENDLINE EOF
    |           NEWLINE*SINGLE_SPACE*ENTRATAB* fator        ENDLINE EOF
    |           NEWLINE*SINGLE_SPACE*ENTRATAB* expr         ENDLINE EOF
    |           NEWLINE*SINGLE_SPACE*ENTRATAB* stmt         ENDLINE EOF
    ;
stmt:           cmd_a 
    |           cmd_na
    ;
cmd_a:          'if' '(' bool ')' cmd_a 'else' cmd_a # IFelse
    |           'while' '(' bool ')'stmts            # WHILE
    ;
cmd_na:         'if' '(' bool ')' stmts                 # IF
    |           'if' '(' bool ')' cmd_a  'else'  cmd_na # IFelsena
    ;    
tipos_var:      INT                     # INT
        |       CHAR                    # CHAR
        ;
atribuicao:     ID '=' expr;           
bool:           termo              # simpleAtr1
    |           termo GE termo     # GE
    |           termo LE termo     # LE
    |           termo EQ termo     # EQ
    |           termo LT termo     # LT
    |           termo GT termo     # GT                
        ;
expr:            termo              # simpleAtr2
    |            termo ADD termo    # ADD
    |            termo SUB termo    # SUB
    ;
termo:    fator              # simpleAtr3
    |     fator MUL fator    # MUL
    |     fator DIV fator    # DIV
    ;
fator:    DIGIT                         # DIGIT
    |      ID                           # ID
    | '(' expr ')'                      # ParenexprParen
    ;
c_chanel:  SINGLE_SPACE* 'CHAN' ID 'id_comp1' 'id_comp2' NEWLINE;

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
CHAR:   [a-z];
ID:   CHAR+;
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
ENDLINE:SINGLE_SPACE* NEWLINE;
COMMENT: '#' CHAR* NEWLINE -> channel(HIDDEN);
SINGLE_SPACE: ' ';
WS  :   SINGLE_SPACE -> skip;    // Define whitespace rule, toss it out