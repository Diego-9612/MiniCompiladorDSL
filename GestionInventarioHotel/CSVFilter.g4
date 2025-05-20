grammar CSVFilter;

prog: stat+ ;

stat
    : loadStat
    | filterStat
    | aggregateStat
    | printStat
    ;

loadStat: 'load' STRING ';' ;

filterStat: 'filter' 'column' expr ';' ;

aggregateStat: 'aggregate' FUNC_NAME 'column' STRING ('where' expr)? ';' ;

printStat: 'print' ';' ;

expr: expr LOGICAL_OP expr                   #logicalExpr
    | STRING OPERATOR value                  #comparisonExpr
    | STRING 'BETWEEN' value 'AND' value     #betweenExpr
    ;

value: NUMBER | STRING ;

FUNC_NAME: 'COUNT' | 'SUM' | 'AVERAGE' ;
LOGICAL_OP: 'AND' | 'OR' ;
OPERATOR: '>' | '<' | '>=' | '<=' | '==' | '!=' ;

STRING: '"' (~["\r\n])* '"' ;
NUMBER: [0-9]+ ('.' [0-9]+)? ;
WS: [ \t\r\n]+ -> skip ;
