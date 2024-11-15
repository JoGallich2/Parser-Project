grammar Parser1;

prog: s* EOF;

//a line is either a simple statment where we don't worry about indents or a complex one where we do
s: simple_statement | complex_statement;

//variable for simple assignment
simple_statement: assignment | array_assignment;
assignment: VARNAME '=' expr | VARNAME ('+=' | '-=' | '*=' | '/=') expr;
array_assignment: VARNAME '=' '[' expr (',' expr)* ']';
expr: expr ('+' | '-' | '*' | '/' | '%') expr | VARNAME | NUMBER | BOOLEAN | STRING | '('expr')';

//variable for complex assignments like if or while
complex_statement: if_statement;

//if, elif, and else statements
if_statement: 'if' condition ':' NEWLINE INDENT block DEDENT (elif_statement)* (else_statement)?;
elif_statement: 'elif' condition ':' NEWLINE INDENT block DEDENT;
else_statement: 'else:' NEWLINE INDENT block DEDENT;

//complex aspects of complex assignments
block: s+;
condition: logical_expr;
logical_expr: not_expr (('and' | 'or') not_expr)*;
not_expr: 'not' comparison_expr | comparison_expr;
comparison_expr: expr (('<' | '<=' | '>' | '>=' | '==' | '!=') expr)?;


//things
VARNAME: [a-zA-Z_][a-zA-Z_0-9]*;
NUMBER: '-'? [0-9]+ ('.'[0-9]+)?;
STRING: '"' .*? '"' | '\'' .*? '\'';
BOOLEAN: 'True' | 'False';
NEWLINE: ('\r'? '\n') -> channel(HIDDEN);
COMMENT: '#' ~[\r\n]* -> skip;
WS: [\t]+ -> skip;

//handling indents
INDENT: SPACES+ {pushIndent(getText().length())}?;
DEDENT: {popIndent()}?;
SPACES: [ ]+ -> channel(HIDDEN);

