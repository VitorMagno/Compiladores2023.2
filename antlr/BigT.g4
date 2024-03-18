grammar BigT;

start: programa_minipar
    ;
programa_minipar:	bloco_stmt* EOF
            ;
bloco_stmt:         bloco_seq
        |           bloco_par
        ;
bloco_seq:          SEQ AC stmts* FC;
bloco_par:          PAR AC stmts* FC;
c_chanel:           CHAN AP id VIRG id VIRG id FP ENDLINE # chan;
print:              PRINT AP id FP ENDLINE # prin;
funcao:             id AP args FP  ENDLINE 
    |               c_chanel        
    |               print           
    ;
atribuicao:         id ASSIGN (expr | comparador) ENDLINE;
stmts:              atribuicao      #atr
    |               comparacao      #comp
    |               repeticao       #rep
    |               funcao          #func
    ;
args:               id(VIRG id)*;
comparacao:         comparacao_comp (ELSE comparacao_comp)* (ELSE AC stmts* FC)?;
comparacao_comp:    IF AP comparador FP AC stmts* FC;
repeticao:          WHILE AP comparador FP AC stmts* FC; 
expr:            fator            # simpleAtr2
    |            AP expr FP       # ParenexprParen
    |            expr MUL expr    # MUL
    |            expr DIV expr    # DIV
    |            expr ADD expr    # ADD
    |            expr SUB expr    # SUB 
    ;
comparador:      comparador_comp (comparador_rep comparador_comp)*
    ;
comparador_comp:    expr GT expr     # GT                             
    |               expr LT expr     # LT 
    |               expr GE expr     # GE 
    |               expr LE expr     # LE 
    |               expr EQ expr     # EQ 
    ;
comparador_rep: AND | OR ;
fator:    int                         
    |     id                           
    ;
int:    INTEGER;
id:     ID;

// parser rules start with lowercase letters, lexer rules with uppercase
WS:   [ \t\r\n]+ -> skip;    
COMMENT: '#' CHAR* '#' -> channel(HIDDEN);
VIRG: ',';
AP: '(';
FP: ')';
AC: '{';
FC: '}';
ASSIGN: '=';
AND:   '&&';
OR:    '||';
GE:    '>=';
LE:    '<=';
EQ:    '==';
LT:    '<';
GT:    '>';
MUL:   '*';                   
DIV:   '/';
ADD:   '+';
SUB:   '-';
PRINT: 'print';
CHAN: 'chan';
ENDLINE: ';';
SEQ: 'SEQ';
PAR: 'PAR';
IF: 'if';
ELSE: 'else';
WHILE: 'while';
fragment CHAR:  [a-z];
fragment INT:   [0-9];
INTEGER: INT+;
ID: CHAR+;
