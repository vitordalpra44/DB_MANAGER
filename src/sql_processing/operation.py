import csv

def load_tbl(filename):
    with open(filename, 'r') as f:
        reader = csv.reader(f, delimiter= ',')
        return reader

def where_operation(where_val1, where_val2, reader):
    with open('result.csv', 'w', newline= '') as result:
        writer = csv.writer
        for row in reader:
            if (reader[where_val1] == where_val2):
                writer.writerow(row)

        

def join_operation(tbl1, tbl2, value):
    print('hello')
