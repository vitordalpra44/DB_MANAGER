import keywords
import lexer

class Node:
    def __init__(self, node_type, value=None):
        self.node_type = node_type
        self.value = value
        self.children = []

    def print_tree(self, indent=""):
        print(f"{indent}{self.node_type}: {self.value}")
        for child in self.children:
            child.print_tree(indent + "\t")

def parse_select(tokens):
    root = Node("MOXTRAI")
    current_node = root
    for token_type, token_value in tokens:
        if token_type == "COLUMN":
            current_node.children.append(Node("COLUMN", token_value))
        elif token_type == "TABLE":
            current_node.children.append(Node("TABLE", token_value))
        elif token_type == "OPERATION":
            current_node.children.append(Node("OPERATION", token_value))
        elif token_type == "VALUE":
            current_node.children.append(Node("VALUE", token_value))
        elif token_type == "KEYWORD" and token_value.upper() in keywords.keywords_node:
            new_node = Node(token_value.upper())
            root.children.append(new_node)
            current_node = new_node
        elif token_type == "KEYWORD" and token_value.upper() in keywords.keywords:
            current_node.children.append(Node(token_value.upper()))
    return root

def parse_delete(tokens):
    root = Node("APAGAÍ")


    current_node = root
    for token_type, token_value in tokens:
        if token_type == "COLUMN":
            current_node.children.append(Node("COLUMN", token_value))
        elif token_type == "TABLE":
            current_node.children.append(Node("TABLE", token_value))
        elif token_type == "OPERATION":
            current_node.children.append(Node("OPERATION", token_value))
        elif token_type == "VALUE":
            current_node.children.append(Node("VALUE", token_value))
        elif token_type == "KEYWORD" and token_value.upper() in keywords.keywords_node:
            new_node = Node(token_value.upper())
            root.children.append(new_node)
            current_node = new_node
        elif token_type == "KEYWORD" and token_value.upper() in keywords.keywords:
            current_node.children.append(Node(token_value.upper()))

    return root

def parse_insert(tokens):
    root = Node("BOTAÍ")
    current_node = root
    values_node = None
    i=0
    for token_type, token_value in tokens:
        if token_type == "TABLE":
            new_node = Node("TABLE", token_value)
            current_node.children.append(new_node)
            current_node = new_node
        elif token_type == "NAME_COLUMN":
            current_node.children.append(Node("NAME_COLUMN", token_value))
        elif token_type == "VALUE_COLUMN":
            new_node = Node("VALUE_COLUMN", token_value)
            current_node.children.append(new_node)
        elif token_type == "NEW_VALUE" and values_node:
            new_node = Node(f"VALUE_{i}")
            i +=1
            current_node = new_node
            values_node.children.append(new_node)
        elif token_type == "KEYWORD" and token_value.upper() == keywords.keyword_values:
            new_node = Node(token_value.upper())
            root.children.append(new_node)
            values_node = new_node
            current_node = new_node

    return root

def parse_update(tokens):
    root = Node("ARRUMAÍ")


    current_node = root
    for token_type, token_value in tokens:
        if token_type == "COLUMN":
            current_node.children.append(Node("COLUMN", token_value))
        elif token_type == "TABLE":
            current_node.children.append(Node("TABLE", token_value))
        elif token_type == "OPERATION":
            current_node.children.append(Node("OPERATION", token_value))
        elif token_type == "VALUE":
            current_node.children.append(Node("VALUE", token_value))
        elif token_type == "KEYWORD" and token_value.upper() in keywords.keywords_node:
            new_node = Node(token_value.upper())
            root.children.append(new_node)
            current_node = new_node
        elif token_type == "KEYWORD" and token_value.upper() in keywords.keywords:
            current_node.children.append(Node(token_value.upper()))

    return root

def parser(query):

    lexerObj = lexer.Lexer(query)
    lexerObj.tokenize()
    tokens = lexerObj.get_tokens()

    if tokens[0][1] == keywords.keyword_select:
        return parse_select(tokens)
    elif tokens[0][1] == keywords.keyword_delete_from:
        return parse_delete(tokens)
    elif tokens[0][1] == keywords.keyword_insert_into:
        return parse_insert(tokens)
    elif tokens[0][1] == keywords.keyword_update:
        return parse_update(tokens)
    else:
        print("Query is not parseable")