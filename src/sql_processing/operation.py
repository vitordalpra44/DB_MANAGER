import csv

# Carrega uma tabela a partir do endereço do arquivo (tabela a ser carregada)
def load_tbl(table):
    with open(table, 'r') as f:
        reader = csv.reader(f, delimiter=',')
        return list(reader)

# Realiza o produto cartesiano entre duas tabelas (tabela 1, tabela 2)
def cartesian (tbl1, tbl2):
    tbl_result = []

    tbl_result.append(tbl1[0] + tbl2[0])
    for a in range(1, len(tbl1)):
        for b in range(1, len(tbl2)):
            tbl_result.append(tbl1[a] + tbl2[b])

    return tbl_result

# Filtra as entradas de uma tabela com base em duas colunas relacinadas por um operador (tabela, coluna 1, coluna 2, operações ('=', '!', '<', '>'))
def filter_column (tbl, col1, col2, op):
    tbl_result = []
    tbl_result.append(tbl[0])

    if op == '=':
        for row in range(1, len(tbl)):
            if tbl[row][col1] == tbl[row][col2]:
                tbl_result.append(tbl[row])
    elif op == '!':
        for row in range(1, len(tbl)):
            if tbl[row][col1] != tbl[row][col2]:
                tbl_result.append(tbl[row])
    elif op == '<':
        for row in range(1, len(tbl)):
            if tbl[row][col1] < tbl[row][col2]:
                tbl_result.append(tbl[row])
    elif op == '>':
        for row in range(1, len(tbl)):
            if tbl[row][col1] > tbl[row][col2]:
                tbl_result.append(tbl[row])

    return tbl_result

# Filtra as entradas de uma tabela com base na comperação de uma coluna com um dado valor (tabela, coluna, valor, operações ('=', '!', '<', '>'))
def filter_value (tbl, col, val, op):
    tbl_result = []
    tbl_result.append(tbl[0])

    if op == '=':
        for row in range(1, len(tbl)):
            if tbl[row][col] == val:
                tbl_result.append(tbl[row])
    elif op == '!':
        for row in range(1, len(tbl)):
            if tbl[row][col] != val:
                tbl_result.append(tbl[row])
    elif op == '<':
        for row in range(1, len(tbl)):
            if tbl[row][col] < val:
                tbl_result.append(tbl[row])
    elif op == '>':
        for row in range(1, len(tbl)):
            if tbl[row][col] > val:
                tbl_result.append(tbl[row])

    return tbl_result

# Ordena as entradas de uma tabela com base em uma coluna (tabela, coluna, ordem descendente (booleano))
def order (tbl, col, desc = False):
    tbl.sort(key = lambda x : x[col], reverse= desc)

# Filtra quais colunas estão presentes em uma tabela (tabela, colunas(lista cotendo os int das colunas))
def column_selection(tbl, cols):
    tbl_result = []

    for row in tbl:
        n_row = []
        col_count = 0
        for c in row:
            if col_count in cols:
                n_row.append(c)
            col_count += 1
        tbl_result.append(n_row)
    
    return tbl_result

#-----------------------------------------------------------#
# Algumas funções a mais para se auxiliar na aplicação

# Deleta uma linha com base em uma tabela secundária filtrada da primeira (tabela, tabela filtrada)
def delete_row(tbl, tbl_filter):
    counter = 0
    for row in tbl:
        if row in tbl_filter:
            tbl.pop(counter)
        counter += 1

# Atualiza tabela segundo uma versão filtrada da mesma , um valor e como essse valor será aplicado na atualização (tabela, tabela filtrada, coluna, valor,
#  operação(None para substituição, '*' para multiplicar o valor presente e '+' para adicionar ao valor presente))
def update_tbl (tbl, tbl_filter, col, val, op = None):
        
    if (op == '*'):    
        for row in tbl:
            if row in tbl_filter:
                row[col] = row[col] * val

    elif (op == '+'):
        for row in tbl:
            if row in tbl_filter:
                row[col] = row[col] + val

    else:
        for row in tbl:
            if row in tbl_filter:
                row[col] = val

# Retorna o índice da coluna em que se encontra um dado valor (tabela, valor)
def return_column_n (tbl, val):
    
    count = 0
    
    for a in tbl[0]:
        if tbl[0][a] == val:
            return count
    count += 1
    
    return (-1)

# Retorna uma lista de índices onde se encontram os valores da lista de entrada (tabela, valores (lista))
def column_list (tbl, vals):
    
    list = []

    for val in vals:
        list.append(return_column_n(tbl, val))
    
    return list

# --------------Exemplo e testes---------------------#

tbl = load_tbl(r'../../databases/University/teaches.csv')

tbl_f = filter_value(tbl, 4, '2017', '=')

update_tbl(tbl, tbl_f,  2, 40)

for row in tbl:
    print(row)

print("\n\n\n")
for row in tbl_f:
    print(row)