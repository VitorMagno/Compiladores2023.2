grammar bigT;		

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
expr:           termo mais_expr;
mais_expr:      ('+'|'-') termo mais_expr;
termo:          fator mais_termo;
mais_termo:     ('*'|'/') fator mais_termo;
fator:          DIGIT | '(' expr ')';
c_chanel:       CHAN ID ID_COMP1 ID_COMP2;

NEWLINE : [\r\n]+ -> skip;
INT     : [0-9]+ ;