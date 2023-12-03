import sys
sys.path.append("../src/sql_processing")
from operation import *

# --------------Exemplo e testes---------------------#

tbl = load_tbl(r'../databases/University/teaches.csv')
indice = find_column_index(tbl, 'teaches', 'year')
print(f"indice {indice}")
#
#tbl_f = filter_value(tbl, 4, '2017', '=')
#
#update_tbl(tbl, tbl_f,  2, 40)
#
#for row in tbl:
#    print(row)
#
#print("\n\n\n")
#for row in tbl_f:
#    print(row)