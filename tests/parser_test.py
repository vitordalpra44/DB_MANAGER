import sys
sys.path.append("../src/sql_processing")

from parser_class import parse_select, parse_delete, parse_insert
import lexer

querySelect = "Select coluna_1, coluna_2, coluna_3 from tabela_1, tabela_2, tabela_3 join tabela_4 on coluna_4 = coluna_5 join tabela_5 using coluna_6 where coluna_7 = coluna_8 and coluna_9 = coluna_10 or coluna_11 = coluna_12 order_by coluna_13 = coluna_14; "
queryDelete = "Delete from tabela_1 join tabela_4 on coluna_4 = coluna_5 join tabela_5 using coluna_6 where coluna_7 = coluna_8 and coluna_9 = coluna_10 or coluna_11 = coluna_12 or coluna_13 = coluna_14 "
queryInsert = "Insert into tabela_1 ( coluna_1, coluna_2 ) values (valor_1, valor_2);"
lexerV = lexer.Lexer(querySelect)
lexerV.tokenize()
tokens = lexerV.get_tokens()
print("Tipo: " + lexerV.type)

for token in tokens:
    print(token)

syntax_tree = parse_select(tokens)
syntax_tree.print_tree()