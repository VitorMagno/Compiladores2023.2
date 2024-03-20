grammar BigT;

start: programa_minipar
    ;
programa_minipar:	bloco_stmt* EOF
            ;
bloco_stmt:         bloco_seq+
        |           bloco_par+
        ;
bloco_seq:          SEQ AC stmts* FC;
bloco_par:          PAR AC stmts* FC;
c_chanel:           CHAN AP id VIRG id VIRG id FP ENDLINE # chan;
print:              PRINT AP id FP ENDLINE # prin;
funcao:             c_chanel        
    |               print           
    ;
atribuicao:         id ASSIGN (expr | comparador) ENDLINE;
stmts:              atribuicao      #atr
    |               comparacao      #comp
    |               repeticao       #rep
    |               funcao          #func
    ;
comparacao:         comparacao_comp (ELSE comparacao_comp)* (ELSE AC stmts* FC)?;
comparacao_comp:    IF AP comparador FP AC stmts* FC;
repeticao:          WHILE AP comparador FP AC stmts* FC; 
expr:            fator            # simpleAtr2
    |            AP expr FP       # ParenexprParen
    |            left=expr MUL right=expr    # MUL
    |            left=expr DIV right=expr    # DIV
    |            left=expr ADD right=expr    # ADD
    |            left=expr SUB right=expr    # SUB 
    ;
comparador:      comparador_comp (comparador_rep comparador_comp)*
    ;
comparador_comp:    left=expr GT right=expr     # GT                             
    |               left=expr LT right=expr     # LT 
    |               left=expr GE right=expr     # GE 
    |               left=expr LE right=expr     # LE 
    |               left=expr EQ right=expr     # EQ 
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
