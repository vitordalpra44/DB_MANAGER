import sys
sys.path.append("../src/sql_processing")

from parser_class import *
from tree_func import *

import lexer
import queries

lexerV = lexer.Lexer(queries.queryUpdate)
lexerV.tokenize()
tokens = lexerV.get_tokens()

syntax_tree = parse_update(tokens)
syntax_tree.print_tree()

tables = []
tree_operation_tables(tokens, tables)

print("\n\n\n")
print(tables)