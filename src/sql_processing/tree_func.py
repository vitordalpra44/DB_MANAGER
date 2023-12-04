from parser_class import *
from operation import *
import keywords
def tree_operation_tables(root, tables):
    for child in root.children:
        if child.children:
            tables = tree_operation_tables(child, tables)
        else:
            if child.node_type == 'TABLE' and child.value not in tables and child.value != "*":
                tables.append(child.value)
                
    return tables

def tree_operation_cartesian(root):
    tables_name = []
    tables_name = tree_operation_tables(root, tables_name)
    tables = []
    table_result = [[""],[""]]
    for table_name in tables_name:
        table_aux = load_tbl(table_name)
        tables.append(table_aux)

    if len(tables_name) >= 2:

        for table in tables:
            table_result = cartesian(table, table_result)
    elif tables:
        table_result = tables[0]
    return table_result

def tree_operation_where(root, table):
    where_operations = []
    table1 = ""
    table2 = ""
    operation = ""
    column1 = ""
    column2 = ""
    i = 0
    where_node = ""
    for node in root.children:
        if node.node_type == keywords.keyword_where:
            where_node = node
    if(where_node):
        while i < len(where_node.children):
            if where_node.children[i].node_type == 'TABLE':
                table1 = where_node.children[i].value
                column1 = where_node.children[i + 1].value
                operation = where_node.children[i + 2].value
                if where_node.children[i + 3].node_type == 'TABLE':
                    table2 = where_node.children[i + 3].value
                    column2 = where_node.children[i + 4].value
                    i += 4
                else:
                    table2 = -1
                    column2 = where_node.children[i + 3].value
                    i += 3
            elif where_node.children[i].node_type != keywords.keyword_and.upper() and where_node.children[i].node_type != keywords.keyword_or.upper():
                table1 = -1
                column1 = where_node.children[i].value
                operation = where_node.children[i + 1].value
                if where_node.children[i + 2].node_type == 'TABLE':
                    table2 = where_node.children[i + 2].value
                    column2 = where_node.children[i + 3].value
                    i += 3
                else:
                    table2 = -1
                    column2 = where_node.children[i + 2].value
                    i += 2
            elif where_node.children[i].node_type == keywords.keyword_and.upper():
                table1 = -2
                table2 = -2
                operation = keywords.keyword_and
                column1 = -2
                column2 = -2
            elif where_node.children[i].node_type == keywords.keyword_or.upper():
                table1 = -2
                table2 = -2
                operation = keywords.keyword_or
                column1 = -2
                column2 = -2
            where_operations.append((table1, column1, operation, table2, column2))
            i += 1

        return where_execution(table, where_operations)
    else:
        return table

def tree_one_operation_join(root):
    
    table1 = ""
    table2 = ""
    operation = ""
    column1 = ""
    column2 = ""
    
    if root.children[1].node_type == keywords.keyword_on:
        table1 = root.children[2].value
        column1 = root.children[3].value
        operation = root.children[4].value
        table2 = root.children[5].value
        column2 = root.children[6].value
    elif root.children[1].node_type == keywords.keyword_using:
        table1 = root.children[2].value
        column1 = root.children[3].value
        operation = '='
        table2 = root.children[0].value
        column2 = root.children[3].value
    
    return (table1, column1, operation, table2, column2)

def tree_operation_join_list(root, table):
    list_join = []
    for node in root.children:
        if node.node_type == keywords.keyword_join:
            list_join.append(tree_one_operation_join(node))
    if list_join:

        return join_filter_execution(table, list_join)
    else:
        return table

def tree_operation_order_by(root, table):
    for node in root.children:
        if node.node_type == keywords.keyword_order_by:
            return order(table, node.children[0].value, node.children[1].value)
    return table

def tree_operation_select_columns(root, tbl):
    column_list = []
    i= 0
    for node in root.children:
        if node.node_type == keywords.keyword_select:
            while i < len(node.children) :
                if node.children[i+1].value == "*":
                    return  column_selection(tbl, -2)#todas as colunas
                else:
                    column_list.append(find_column_index(tbl, node.children[i].value, node.children[i+1].value))
                    i+=1
                i += 1
            if column_list:
                table = column_selection(tbl, column_list)
                return table
    return tbl

def tree_operation_insert_values(root):
    register = []
    register_list = []
    for node in root.children:
        if node.node_type == keywords.keyword_values:
            for nodinho in node.children:
                register = []
                for nodizinho in nodinho.children:
                    register.append(nodizinho.value)
                register_list.append(register)
    return register_list
            
    

def tree_operation_select(root):
    table_1 = tree_operation_cartesian(root)
    table_2 = tree_operation_where(root, table_1)
    table_3 = tree_operation_join_list(root, table_2)
    table_4 = tree_operation_order_by(root, table_3)
    table_5 = tree_operation_select_columns(root, table_4)
    return table_5

def tree_operation_delete(root):
    table_1 = tree_operation_cartesian(root)
    table_2 = tree_operation_where(root, table_1)
    table_1 = delete_row(table_1, table_2)
    save_tbl(root.children[1].value,table_1)

def tree_operation_insert(root):
    table_1 = tree_operation_cartesian(root)
    values = tree_operation_insert_values(root)
    for row in values:
        table_1.append(row)
    save_tbl(root.children[1].value,table_1)

def tree_operation_update(root):
    table_1 = tree_operation_cartesian(root)
    table_2 = tree_operation_where(root, table_1)

    for row in table_2:
        print(row)
    column = ""
    table = ""
    val = ""
    operation = ""
    for node in root.children:
        if node.node_type == keywords.keyword_update:
            table = node.children[0].value
    for node in root.children:
        if node.node_type == keywords.keyword_set:
            column = node.children[0].value
            operation = node.children[1].value
            val = node.children[2].value
    col = find_column_index(table_1, table, column)
    print(col)
    print(table)
    print(col)
    print(val)
    print(operation)
    update_tbl(table_1, table_2, col, val, operation)
    save_tbl(table, table_1)

def tree_operation(query):
    root = parser(query)
    if root.node_type == keywords.keyword_select:
        return tree_operation_select(root)
    elif root.node_type == keywords.keyword_delete_from:
        tree_operation_delete(root)
        return -1
    elif root.node_type == keywords.keyword_insert_into:
        tree_operation_insert(root)
        return -1
    elif root.node_type == keywords.keyword_update:
        tree_operation_update(root)
        return -1
    

