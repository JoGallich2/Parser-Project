grammar Deliverable1;

// Top-level rule for a program
prog: s* EOF;

// Statements
s: assignment 
 | array_assignment;

// Assignment operations (simple and compound)
assignment: VARNAME '=' expr | VARNAME ('+=' | '-=' | '*=' | '/=') expr;

// Array assignments with potential multiple expressions
array_assignment: VARNAME '=' '[' (expr (',' expr)*)? ']';

// Expression rules
expr: expr ('+' | '-' | '*' | '/' | '%') expr   // Arithmetic
    | VARNAME   // Variable reference
    | NUMBER    // Number literal
    | BOOLEAN   // Boolean literal
    | STRING    // String literal
    | '(' expr ')'  // Parentheses for grouping
    ;

// Variable naming rule matching Python variable naming rules
VARNAME: [a-zA-Z_][a-zA-Z_0-9]*;

// Number literal, supports decimals
NUMBER: '-'? [0-9]+ ('.'[0-9]+)?;

// Boolean literals
BOOLEAN: 'True' | 'False';

// String literals (single or double-quoted)
STRING: '"' .*? '"' | '\'' .*? '\'';

// Skip whitespace and newlines
WS: [ \t\r\n]+ -> skip;

// Support comments (e.g., # This is a comment)
COMMENT: '#' ~[\r\n]* -> skip;
