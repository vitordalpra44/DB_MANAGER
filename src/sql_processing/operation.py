import csv

def load_tbl(table):
    with open(table, 'r') as f:
        reader = csv.reader(f, delimiter=',')
        return list(reader)

def cartesian (tbl1, tbl2):
    tbl_result = []

    tbl_result.append(tbl1[0] + tbl2[0])
    for a in range(1, len(tbl1)):
        for b in range(1, len(tbl2)):
            tbl_result.append(tbl1[a] + tbl2[b])

    return tbl_result

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

def order (tbl, col, desc = False):
    tbl.sort(key = lambda x : x[col], reverse= desc)

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
# Funcs extras caso necessário

def return_column_n (tbl, val):
    
    count = 0
    
    for a in tbl[0]:
        if tbl[0][a] == val:
            return count
    count += 1
    
    return (-1)

def column_list (tbl, vals):
    
    list = []

    for val in vals:
        list.append(return_column_n(tbl, val))
    
    return list