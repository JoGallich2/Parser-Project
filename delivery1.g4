grammar delivery1;

start: (dclr | expr) EOF
	 ;

dclr: TYPE VARNAME ('='| '+=' | '-=' | '*=' | '/=') expr
	;

expr: expr '*' expr
	| expr '/' expr
	| expr '+' expr
	| expr '-' expr
	| TYPE
	| NUM
	;

TYPE: 'INT' | 'DOUBLE';
VARNAME : [a-z]*; //lowercase
NUM : '0' | '-'?[1-9][0-9]* //0, -, firstdigit 1-9, second digit+ 0-9
WS : [ \t\r\n]+ -> skip ;