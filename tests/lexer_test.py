import sys
sys.path.append("../src/sql_processing")
import lexer
import queries


lexerV = lexer.Lexer(queries.queryUpdate)
lexerV.tokenize()
tokens = lexerV.get_tokens()
print("Tipo: " + lexerV.type)

for token in tokens:
    print(token)

