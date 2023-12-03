import parser_class
from operation import *
import keywords
def tree_operation_tables(root, tables):
    for child in root.children:
        if child.children:
            tables = tree_operation_tables(child, tables)
        else:
            if child.node_type == 'TABLE' and child.value not in tables:
                tables.append(child.value)
        
    return tables

def tree_operation_join(tables_name):
    tables = []
    table_result = [[""],[""]]
    for table_name in tables_name:
        table_aux = load_tbl(table_name)
        tables.append(table_aux)

    if len(tables_name) >= 2:

        for table in tables:
            table_result = cartesian(table, table_result)
    return table_result

def tree_operation_where(root):
    where_operations = []
    table1 = ""
    table2 = ""
    operation = ""
    column1 = ""
    column2 = ""
    i = 0
    while i < len(root.children):
        if root.children[i].node_type == 'TABLE':
            table1 = root.children[i].value
            column1 = root.children[i + 1].value
            operation = root.children[i + 2].value
            if root.children[i + 3].node_type == 'TABLE':
                table2 = root.children[i + 3].value
                column2 = root.children[i + 4].value
                i += 4
            else:
                table2 = -1
                column2 = root.children[i + 3].value
                i += 3
        elif root.children[i].node_type != keywords.keyword_and.upper() and root.children[i].node_type != keywords.keyword_or.upper():
            table1 = -1
            column1 = root.children[i].value
            operation = root.children[i + 1].value
            if root.children[i + 2].node_type == 'TABLE':
                table2 = root.children[i + 2].value
                column2 = root.children[i + 3].value
                i += 3
            else:
                table2 = -1
                column2 = root.children[i + 2].value
                i += 2
        elif root.children[i].node_type == keywords.keyword_and.upper():
            table1 = -2
            table2 = -2
            operation = keywords.keyword_and
            column1 = -2
            column2 = -2
        elif root.children[i].node_type == keywords.keyword_or.upper():
            table1 = -2
            table2 = -2
            operation = keywords.keyword_or
            column1 = -2
            column2 = -2
        where_operations.append((table1, column1, operation, table2, column2))
        i += 1

    return where_operations

