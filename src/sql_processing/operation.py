import csv
import global_var
import keywords as kw
# Carrega uma tabela a partir do endereço do arquivo (tabela a ser carregada)
def load_tbl(table):
    with open(f"../databases/{global_var.database}/{table}.csv", 'r') as f:
        reader = csv.reader(f, delimiter=';')
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


def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False
    
# Ordena as entradas de uma tabela com base em uma coluna (tabela, coluna, ordem descendente (booleano))
def order (tbl, table_name, column_name):
    col = find_column_index(tbl, table_name, column_name)
    tabela_final = []

    for row in enumerate(tbl, start=1):
        if(row[0] != 1):
            tabela_final.append(row[1])

    tabela_final.sort(key=lambda x: (float(x[col]) if is_float(x[col]) else x[col]))
    tabela_final.insert(0, tbl[0])
    return tabela_final

    
# Filtra quais colunas estão presentes em uma tabela (tabela, colunas(lista cotendo os int das colunas))
def column_selection(tbl, cols):
    tbl_result = []
    if cols == -2:
        return tbl
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
    tbl_result = [row for row in tbl if tuple(row) not in set(map(tuple, tbl_filter))]
    return tbl_result

# Atualiza tabela segundo uma versão filtrada da mesma , um valor e como essse valor será aplicado na atualização (tabela, tabela filtrada, coluna, valor,
#  operação(None para substituição, '*' para multiplicar o valor presente e '+' para adicionar ao valor presente))
def update_tbl (tbl, tbl_filter, col, val, op = None):

    if (op == '*'):
        for a in range(1, len(tbl)):
            if tbl[a] in tbl_filter:
                tbl[a][col] = str(eval(tbl[a][col]) * eval(val))

    elif (op == '+'):
        for a in range(1, len(tbl)):
            if tbl[a] in tbl_filter:
                tbl[a][col] = str(eval(tbl[a][col]) + eval(val))

    else:
        for a in range(1, len(tbl)):
            if tbl[a] in tbl_filter:
                tbl[a][col] = val


# Retorna uma lista de índices onde se encontram os valores da lista de entrada (tabela, valores (lista))
def column_list (tbl, tables, columns):
    
    list = []

    for column, table in zip(columns, tables):
        list.append(find_column_index(tbl, table, column))
    
    return list

#retorna o indice de uma coluna csv com base no nome da tabela e da coluna
def find_column_index(table, table_name, column):
    index = 0
    for column_info in table[0]:
        parts = column_info.split('-')
        
        if len(parts) == 3 and parts[0] == table_name and parts[1] == column:
            return index
        index += 1

    return -1



def Unite_tables (tbl1, tbl2):
    tbl_result = []
    tbl_result = tbl1

    for row in tbl2:
        if row not in tbl_result:
            tbl_result.append(row)

    return tbl_result

def save_tbl(table_name, table):
    with open(f"../databases/{global_var.database}/{table_name}.csv", 'w') as f:
        reader = csv.writer(f)
        for row in table:
            reader.writerow(row)

def where_execution (tbl, command_list):
    tbl_where = []
    tbl_result_and = []
    tbl_result_final = []
    for cmd_row in command_list:
        if cmd_row[2] != kw.keyword_and and cmd_row[2] != kw.keyword_or:
            tbl_where.append(cmd_row)

    where_index = 0
    tbl_aux_and = tbl

    if tbl_where[where_index][0] == -1:
        tbl_aux_and = filter_value(tbl_aux_and, find_column_index(tbl_aux_and, tbl_where[where_index][3], tbl_where[where_index][4]), tbl_where[where_index][1], tbl_where[where_index][2])
    if tbl_where[where_index][3] == -1:
        tbl_aux_and = filter_value(tbl_aux_and, find_column_index(tbl_aux_and, tbl_where[where_index][0], tbl_where[where_index][1]), tbl_where[where_index][4], tbl_where[where_index][2])
    else:
        tbl_aux_and = filter_column(tbl_aux_and, find_column_index(tbl_aux_and, tbl_where[where_index][0], tbl_where[where_index][1]),find_column_index(tbl, tbl_where[where_index][3], tbl_where[where_index][4]), tbl_where[where_index][2])
    where_index += 1

    for cmd_row in command_list:
        if cmd_row[2] == kw.keyword_and:
            if tbl_where[where_index][0] == -1:
                tbl_aux_and = filter_value(tbl_aux_and, find_column_index(tbl_aux_and, tbl_where[where_index][3], tbl_where[where_index][4]), tbl_where[where_index][1], tbl_where[where_index][2])
            if tbl_where[where_index][3] == -1:
                tbl_aux_and = filter_value(tbl_aux_and, find_column_index(tbl_aux_and, tbl_where[where_index][0], tbl_where[where_index][1]), tbl_where[where_index][4], tbl_where[where_index][2])
            else:
                tbl_aux_and = filter_column(tbl_aux_and, find_column_index(tbl_aux_and, tbl_where[where_index][0], tbl_where[where_index][1]),find_column_index(tbl, tbl_where[where_index][3], tbl_where[where_index][4]), tbl_where[where_index][2])
                #TÁ certo
                #for i in tbl_aux_and:
                #    print(i)

            where_index += 1

        elif cmd_row[2] == kw.keyword_or:
            tbl_result_and.append(tbl_aux_and)
            tbl_aux_and = tbl
            if tbl_where[where_index][0] == -1:
                tbl_aux_and = filter_value(tbl_aux_and, find_column_index(tbl_aux_and, tbl_where[where_index][3], tbl_where[where_index][4]), tbl_where[where_index][1], tbl_where[where_index][2])
            if tbl_where[where_index][3] == -1:
                tbl_aux_and = filter_value(tbl_aux_and, find_column_index(tbl_aux_and, tbl_where[where_index][0], tbl_where[where_index][1]), tbl_where[where_index][4], tbl_where[where_index][2])
            else:
                tbl_aux_and = filter_column(tbl_aux_and, find_column_index(tbl_aux_and, tbl_where[where_index][0], tbl_where[where_index][1]),find_column_index(tbl, tbl_where[where_index][3], tbl_where[where_index][4]), tbl_where[where_index][2])
            where_index += 1

    tbl_result_and.append(tbl_aux_and)

    and_index = 0

    for cmd_row in command_list:
        if cmd_row[2] == kw.keyword_or:
            tbl_result_final = Unite_tables(tbl_result_final, tbl_result_and[and_index])
            and_index += 1

    tbl_result_final = Unite_tables(tbl_result_final, tbl_result_and[and_index])

    return tbl_result_final



def join_filter_execution (tbl, command_list):

    tbl_result = tbl
    for row in command_list:
            print(row)
            tbl_result = filter_column (tbl_result, find_column_index(tbl_result, row[0], row[1]), find_column_index(tbl_result, row[3], row[4]), row[2])
    return tbl_result