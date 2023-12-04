import sys
sys.path.append("../src/sql_processing")

from parser_class import *

import lexer
import queries

lexerV = lexer.Lexer(queries.querySelect)
lexerV.tokenize()
tokens = lexerV.get_tokens()

syntax_tree = parse_select(tokens)
syntax_tree.print_tree()
