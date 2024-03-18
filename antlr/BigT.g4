grammar BigT;

start: programa_minipar
    ;
programa_minipar:	bloco_stmt* EOF
            ;
bloco_stmt:     bloco_seq
        |       bloco_par
        ;
bloco_seq:      'SEQ' '{' (stmts)* '}';
bloco_par:      'PAR' '{' (stmts)* '}';
stmts:          atribuicao ENDLINE
    |           fator      ENDLINE
    |           expr       ENDLINE
    |           stmt       ENDLINE
    ;
stmt:           cmd_a 
    |           cmd_na
    ;
cmd_a:          'if' '(' expr ')' '{' cmd_a '}' 'else' '{' cmd_a '}'# IFelse
    |           'while' '(' expr ')'stmts            # WHILE
    ;
cmd_na:         'if' '(' expr ')' '{'stmts '}'                # IF
    |           'if' '(' expr ')' '{'cmd_a '}' 'else' '}' cmd_na '}'# IFelsena
    ;    
tipos_var:      INT                     # INT
        |       CHAR                    # CHAR
        ;
atribuicao:     ID '=' expr      
        ;
expr:            fator            # simpleAtr2
    |            '(' expr ')'     # ParenexprParen
    |            expr '*' expr    # MUL
    |            expr '/' expr    # DIV
    |            expr '+' expr    # ADD
    |            expr '-' expr    # SUB 
    |            expr '>=' expr     # GE
    |            expr '<=' expr     # LE
    |            expr '==' expr     # EQ
    |            expr '<' expr     # LT
    |            expr '>' expr     # GT                            
    ;
fator:    DIGIT                         # DIGIT
    |      ID                           # ID
    ;
c_chanel:  'CHAN' ID 'id_comp1' 'id_comp2'ENDLINE;

// parser rules start with lowercase letters, lexer rules with uppercase
WS:   [ \t\r\n]+ -> skip;    // Define whitespace rule, toss it out
COMMENT: '#' CHAR* NEWLINE -> channel(HIDDEN);
AND:   '&&';
OR:    '||';
NOT:    '!';
GE:    '>=';
LE:    '<=';
EQ:    '==';
LT:     '<';
GT:    '>';
MUL:   '*';                   // assigns token name to '*' used above in grammar
DIV:   '/';
ADD:   '+';
SUB:   '-';
CHAR:   [a-z];
ID:   [a-zA-Z_]+;
INT:   [0-9]+ ;
DIGIT: CHAR+([0-9]*|[a-zA-Z]*)|INT;
CHAN: [CHAN];
ID_COMP1: CHAR+([0-9]*|[a-zA-Z]*);
ID_COMP2: CHAR+([0-9]*|[a-zA-Z]*);
NEWLINE: [\r\n]+;
ENDLINE: ';';
SEQ:   [SEQ];
PAR:   [PAR];