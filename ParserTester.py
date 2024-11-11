from antlr4 import *
from Deliverable1Lexer import Deliverable1Lexer
from Deliverable1Parser import Deliverable1Parser
from antlr4.error.ErrorListener import ErrorListener

class SyntaxErrorListener(ErrorListener):
    def __init__(self):
        super(SyntaxErrorListener, self).__init__()
        self.errors = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.errors.append(f"Syntax error at line {line}, column {column}: {msg}")

test_code = """
assign1 = "20"
assign2 = 123
assign3 = 1.23
assign4 = assign1

arith_op1 = 1 + 2
arith_op2 = 13 - 3
arith_op3 = 10 / arith_op1
arith_op4 = 4.2 * 10
arith_op5 = arith_op1 % arith_op2

arith_op1 += arith_op2
arith_op2 -= arith_op3
arith_op3 *= arith_op4
arith_op4 /= arith_op5

array1 = [1, 2, 3, 4, 5]
array2 = ['a', 'b', 'c']
array3 = [1.6, 2.7, 3.8, 4.9, 5.0]

var1 = 10
var2 = var1/2 + 5
var3 = var2 % 2
var4 = 1

flag = True
"""

input_stream = InputStream(test_code)
lexer = Deliverable1Lexer(input_stream)
stream = CommonTokenStream(lexer)
parser = Deliverable1Parser(stream)

# Add custom error listener
error_listener = SyntaxErrorListener()
parser.removeErrorListeners()
parser.addErrorListener(error_listener)

tree = parser.prog()

# Output results
if error_listener.errors:
    print("Errors found:")
    for error in error_listener.errors:
        print(error)
else:
    print("No syntax errors.")
