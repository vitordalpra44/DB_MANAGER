class Node:
    def __init__(self, node_type, value=None):
        self.node_type = node_type
        self.value = value
        self.children = []

    def print_tree(self, indent=""):
        print(f"{indent}{self.node_type}: {self.value}")
        for child in self.children:
            child.print_tree(indent + "  ")

def parse_select(tokens):
    root = Node("SELECT")
    current_node = root

    for token_type, token_value in tokens:
        if token_type == "COLUMN":
            current_node.children.append(Node("COLUMN", token_value))
        elif token_type == "TABLE":
            current_node.children.append(Node("TABLE", token_value))
        elif token_type == "JOIN_VAR":
            current_node.children.append(Node("JOIN_VAR", token_value))
        elif token_type == "ON_VAR":
            current_node.children.append(Node("ON_VAR", token_value))
        elif token_type == "USING_VAR":
            current_node.children.append(Node("USING_VAR", token_value))
        elif token_type == "WHERE_VAR":
            current_node.children.append(Node("WHERE_VAR", token_value))
        elif token_type == "ORDER_BY_VAR":
            current_node.children.append(Node("ORDER_BY_VAR", token_value))
        elif token_type == "KEYWORD" and token_value.upper() in ["FROM", "JOIN", "WHERE", "ORDER_BY", "ON", "USING"]:
            new_node = Node(token_value.upper())
            current_node.children.append(new_node)
            current_node = new_node

    return root

def parse_delete(tokens):
    root = Node("DELETE FROM")
    current_node = root

    for token_type, token_value in tokens:
        if token_type == "TABLE":
            current_node.children.append(Node("TABLE", token_value))
        elif token_type == "JOIN_VAR":
            current_node.children.append(Node("JOIN_VAR", token_value))
        elif token_type == "ON_VAR":
            current_node.children.append(Node("ON_VAR", token_value))
        elif token_type == "USING_VAR":
            current_node.children.append(Node("USING_VAR", token_value))
        elif token_type == "WHERE_VAR":
            current_node.children.append(Node("WHERE_VAR", token_value))
        elif token_type == "KEYWORD" and token_value.upper() in ["JOIN", "WHERE", "ON", "USING"]:
            new_node = Node(token_value.upper())
            current_node.children.append(new_node)
            current_node = new_node

    return root

def parse_insert(tokens):
    root = Node("INSERT INTO")
    current_node = root

    for token_type, token_value in tokens:
        if token_type == "TABLE":
            new_node = Node("TABLE", token_value)
            current_node.children.append(new_node)
            current_node = new_node
        elif token_type == "NAME_COLUMN":
            current_node.children.append(Node("NAME_COLUMN", token_value))
        elif token_type == "VALUE_COLUMN":
            current_node.children.append(Node("VALUE_COLUMN", token_value))
        elif token_type == "KEYWORD" and token_value.upper() in ["VALUES"]:
            new_node = Node(token_value.upper())
            current_node.children.append(new_node)
            current_node = new_node

    return root