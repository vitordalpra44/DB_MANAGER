import sys
sys.path.append("../src/sql_processing")
import lexer

query = "Select coluna_1, coluna_2, coluna_3 from tabela_1, tabela_2, tabela_3 join tabela_4 on coluna_4 = coluna_5 join tabela_5 using coluna_6 where coluna_7 = coluna_8 and coluna_9 = coluna_10 or coluna_11 = coluna_12 order_by coluna_13 = coluna_14 "
lexerV = lexer.Lexer(query)
lexerV.tokenize()
tokens = lexerV.get_tokens()

for token in tokens:
    print(token)