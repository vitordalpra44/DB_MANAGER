#from tree_func import *
import sys
sys.path.append("../src")
sys.path.append("../src/sql_processing")
import global_var
from tree_func import *
from operation import *
from parser_class import *
import lexer
import queries
global_var.database = "University"

tables = ['teaches', 'instructor']
table_result = tree_operation_join(tables)
save_tbl('teste', table_result)

lexerV = lexer.Lexer(queries.queryWhere)
lexerV.tokenize()
tokens = lexerV.get_tokens()

syntax_tree = parse_select(tokens)
syntax_tree.print_tree()
node_where = None
for node in syntax_tree.children:
    if node.node_type == keywords.keyword_where.upper():
        node_where = node

lista = tree_operation_where(node_where)
print("\n\n\nTABELA CRUA:")
for row in table_result:
    print(row)
print("\n\n\nLISTA:")
for row in lista:
    print(row)
    
tabela_final = where_execution(table_result, lista)
print("\n\n\nTABELA WHERE:")
for row in tabela_final:
    print(row)




