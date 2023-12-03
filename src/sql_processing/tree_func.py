import parser_class

def tree_operation_tables(root, tables):
    for child in root.children:
        if child.children:
            tables = tree_operation_tables(child, tables)
        else:
            if child.node_type == 'TABLE' and child.value not in tables:
                tables.append(child.value)
        
    return tables

