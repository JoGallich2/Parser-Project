grammar delivery1;

start: (dclr | expr) EOF
	 ;

dclr: TYPE VARNAME ('='| '+=' | '-=' | '*=' | '/=') expr
	;

expr: expr '*' expr
	| expr '/' expr
	| expr '+' expr
	| expr '-' expr
	| expr '%' expr
	| '(' expr ')'
	| VARNAME
	| TYPE
	| NUM
	;

TYPE: 'INT' | 'DOUBLE';
VARNAME: [a-zA-Z_][a-zA-Z0-9_]* ; //Alphebet Lowercase as well as UpperCase. As well as number 0-9 just not first(Python variable names rules)
NUM : '0' | '-'?[1-9][0-9]* //0, -, firstdigit 1-9, second digit+ 0-9
WS : [ \t\r\n]+ -> skip ;