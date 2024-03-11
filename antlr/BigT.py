import sys
from antlr4 import *
from antlr4.InputStream import InputStream
from build.BigTLexer import BigTLexer
from build.BigTParser import BigTParser
from build.BigTListener import BigTListener
from build.BigTVisitor import BigTVisitor

def main(argv):
    if len(sys.argv) > 1:
        input_stream = FileStream(sys.argv[1])
    else:
        input_stream = InputStream(sys.stdin.readline())
    lexer = BigTLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = BigTParser(stream)
    tree = parser.progama_minipar()

    visitor = BigTVisitor()
    visitor.visit(tree)

if __name__ == '__main__':
    main(sys.argv)