import csv

def load_tbl(table):
    with open(table, 'r') as f:
        reader = csv.reader(f, delimiter=',')
        return list(reader)

def where_operation(where_val1, where_val2, reader, operation, type):
    result_rows = []

    for row in reader:
        if operation == '=' and row[where_val1] == where_val2:
            result_rows.append(row)
        elif operation == '<' and row[where_val1] < where_val2:
            result_rows.append(row)
        elif operation == '>' and row[where_val1] > where_val2:
            result_rows.append(row)
        elif operation == '!' and row[where_val1] != where_val2:
            result_rows.append(row)
        elif operation == 'column' and row[where_val1] == row[where_val2]:
            result_rows.append(row)

    return result_rows

def write_result(result_rows):
    with open('result.csv', 'w', newline='') as result:
        writer = csv.writer(result)
        writer.writerows(result_rows)