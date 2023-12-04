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

root = parser(queries.queryUpdate1)
root.print_tree()

table_select = tree_operation_update(root)


for row in table_select:
    print(row)
print(f"\n\nrows({len(table_select)-1})")


