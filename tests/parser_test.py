import sys
sys.path.append("../src/sql_processing")

from parser_class import *
import lexer
import queries

lexerV = lexer.Lexer(queries.queryUpdate)
lexerV.tokenize()
tokens = lexerV.get_tokens()

syntax_tree = parse_update(tokens)
syntax_tree.print_tree()