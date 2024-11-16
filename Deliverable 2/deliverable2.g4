grammar Deliverable2;

prog: s* EOF;

//a line is either a simple statment where we don't worry about indents or a complex one where we do
s: simple_statement | complex_statement;

//variable for simple assignment
simple_statement: assignment | array_assignment | VARNAME NEWLINE;
assignment: VARNAME '=' expr | VARNAME ('+=' | '-=' | '*=' | '/=') expr;
array_assignment: VARNAME '=' '[' expr (',' expr)* ']';


// Expression rules
expr: expr ('+' | '-' | '*' | '/' | '%') expr   // Arithmetic expressions
    | VARNAME   // Variable reference
    | NUMBER    // Number literal
    | BOOLEAN   // Boolean literal
    | STRING    // String literal
    | '(' expr ')'  // Parentheses for grouping
    ;
//variable for complex assignments like if or while
complex_statement: if_statement;


//if, elif, and else statements
if_statement: 'if' condition ':' block
             (elif_statement)* 
             else_statement?;

elif_statement: 'elif' condition ':' block;

else_statement: 'else' ':' block;


//complex aspects of complex assignments
block: (simple_statement )*;
condition: logical_expr;
logical_expr: not_expr (('and' | 'or') not_expr)*;
not_expr: 'not' comparison_expr | comparison_expr;
comparison_expr: expr (('<' | '<=' | '>' | '>=' | '==' | '!=') expr)?;


// Tokens
VARNAME: [a-zA-Z_][a-zA-Z_0-9]*;
NUMBER: '-'? [0-9]+ ('.'[0-9]+)?;
BOOLEAN: 'True' | 'False';
STRING: '"' .*? '"' | '\'' .*? '\'';
WS: [ \t\r\n]+ -> skip;
TAB: [\t]+;
COMMENT: '#' ~[\r\n]* -> skip;
NEWLINE: ('\r'? '\n') -> channel(HIDDEN);


//handling indents
INDENT: SPACES+ {getIndentationLevel() > getCurrentLevel()}?;
SPACES: [ ]+ -> channel(HIDDEN);