grammar Deliverable1;

// Top-level rule for a program
prog: s* EOF;

// Statements
s: assignment 
  | array_assignment
  ;

// Assignment operations (simple and compound)
assignment: VARNAME '=' expr
          | VARNAME ('+=' | '-=' | '*=' | '/=') expr  // Compound assignment
          ;

// Array assignments with potential multiple expressions
array_assignment: VARNAME '=' '[' (expr (',' expr)*)? ']';

// Conditional expressions
condition: expr ('<' | '<=' | '>' | '>=' | '==' | '!=') expr  // Relational operators
         | expr AND expr                                      // Logical AND
         | expr OR expr                                       // Logical OR
         | NOT expr                                           // Logical NOT
         | '(' condition ')'                                  // Parentheses for grouping
         ;

// Expression rules
expr: expr ('+' | '-' | '*' | '/' | '%') expr   // Arithmetic expressions
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

// For tabs (indentation in Python style)
TAB: [\t]+;

// Support comments (e.g., # This is a comment)
COMMENT: '#' ~[\r\n]* -> skip;