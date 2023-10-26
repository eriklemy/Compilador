#!/usr/bin/env python3

from antlr4 import CommonTokenStream, FileStream
from ParserLexer import ParserLexer
from ParserParser import ParserParser

fileName = "/teste2.txt";

print(f"Arquivo sendo testado: {fileName}\n\n")

input_stream = FileStream(fileName)

# Crie o lexer
lexer = ParserLexer(input_stream)
stream = CommonTokenStream(lexer)

# Crie o parser
parser = ParserParser(stream)

# Inicie a análise no ponto de entrada 'program'
tree = parser.program()

# Imprima a árvore de análise sintática gerada
print(tree.toStringTree())
