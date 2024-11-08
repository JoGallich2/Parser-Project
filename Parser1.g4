grammar Parser1;

//since this is python there are just expressions then nothing so no main
prog: s* EOF;


//you may be wondering, why no end expression? Well python doesn't have those, and so wehn the program reaches a \n the
//parser simply moves to the next line


//need assignment and array assignment since they can't be done in the same line
s: assignment | array_assignment;

//assignments are a either = some expression or +=/*=/... some expression
assignment: VARNAME '=' expr | VARNAME ('+=' | '-=' | '*=' | '/=') expr;

//array assignments are more complicated they must be bound by [] but can have any number of expressions
//that are precedeed by a (,) there can be empty arrays but those are a whole other thing we probably won't be doing
//someone check this
array_assignment: VARNAME '=' '[' expr (',' expr)* ']';

//an expression can be a certain number of options:
//      1. 'expression' 'arithmetic' 'expression', if there's an arithmetic it must be followed b another expression
//      2. Just a variable name
//      3. A data type like a number, a boolean, or a string
expr: expr ('+' | '-' | '*' | '/' | '%') expr | VARNAME | NUMBER | BOOLEAN | STRING;

//in python a variable can start with any letter but never a number
VARNAME: [a-zA-Z_][a-zA-Z_0-9]*;

//a number can be any combination of numbers and can be followed by a decimal
//luckily this is python so decimals don't need to follow a number
NUMBER: [0-9]+ ('.' [0-9]+)?;

//strings are funky I had to look this up I don't really get it
STRING: '"' .*? '"' | '\'' .*? '\'';

//a boolean can be either True or False nothing else
BOOLEAN: 'True' | 'False';

//since we're not thinking about indents yet we ignore them
WS: [ \t\r\n]+ -> skip;