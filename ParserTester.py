import sys
from antlr4 import *
from Deliverable1Parser import Deliverable1Parser
from Deliverable1Lexer import Deliverable1Lexer
from antlr4.tree.Trees import Trees

file_path = "./project_deliverable_1.py"

def main():
    input_stream = FileStream(file_path)
    lexer = Deliverable1Lexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = Deliverable1Parser(token_stream)
    tree = parser.prog()
    print(tree.toStringTree(recog=parser))

main()
    

