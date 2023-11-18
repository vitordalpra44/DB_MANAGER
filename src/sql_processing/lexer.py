class Lexer:
    def __init__(self, query):
        self.query = query
        self.tokens = []

    def tokenize(self):
        current_token = ""
        inside_select_clause = False
        inside_from_clause = False
        inside_join_clause = False
        inside_on_clause = False
        inside_where_clause = False
        inside_order_by_clause = False
        inside_using_clause = False
        for char in self.query:
            if char.isalnum() or char == '_':
                current_token += char
            else:
                if current_token.upper() == "SELECT":
                    inside_select_clause = True
                elif current_token.upper() == "FROM":
                    inside_from_clause = True
                    inside_select_clause = False
                elif current_token.upper() == "JOIN":
                    inside_from_clause = False
                    inside_on_clause = False
                    inside_using_clause = False
                    inside_join_clause = True
                elif current_token.upper() == "ON":
                    inside_join_clause = False
                    inside_on_clause = True
                elif current_token.upper() == "USING":
                    inside_join_clause = False
                    inside_using_clause = True
                elif current_token.upper() == "WHERE":
                    inside_from_clause = False
                    inside_on_clause = False
                    inside_using_clause = False
                    inside_where_clause = True
                elif current_token.upper() == "ORDER_BY":
                    inside_from_clause = False
                    inside_on_clause = False
                    inside_using_clause = False
                    inside_where_clause = False
                    inside_order_by_clause = True
                elif current_token == ";":
                    inside_select_clause = False
                    inside_from_clause = False
                    inside_join_clause = False
                    inside_on_clause = False
                    inside_using_clause = False
                    inside_where_clause = False
                    inside_order_by_clause = False

                if char.isspace() or char in (',', ';', '(', ')', '*', '='):
                    if current_token and (current_token.upper() == "SELECT" or current_token.upper() == "FROM" or current_token.upper() == "JOIN" or current_token.upper() == "WHERE" or current_token.upper() == "USING" or current_token.upper() == "ON" or current_token.upper() == "ORDER_BY" or current_token.upper() == "AND" or current_token.upper() == "OR"):
                        self.tokens.append(("KEYWORD", current_token))
                    elif current_token and inside_select_clause:
                        self.tokens.append(("COLUMN", current_token))
                    elif current_token and inside_from_clause:
                        self.tokens.append(("TABLE", current_token))
                    elif current_token and inside_join_clause:
                        self.tokens.append(("JOIN_VAR", current_token))
                    elif current_token and inside_on_clause:
                        self.tokens.append(("ON_VAR", current_token))
                    elif current_token and inside_using_clause:
                        self.tokens.append(("USING_VAR", current_token))
                    elif current_token and inside_where_clause:
                        self.tokens.append(("WHERE_VAR", current_token))
                    elif current_token and inside_order_by_clause:
                        self.tokens.append(("ORDER_BY_VAR", current_token))
                    elif current_token:
                        self.tokens.append(("UNDEFINED", current_token))
                    if char != ' ':
                        self.tokens.append((char, char))

                    current_token = ""
                

        if current_token:
                    if (current_token.upper() == "SELECT" or current_token.upper() == "FROM" or current_token.upper() == "JOIN" or current_token.upper() == "WHERE" or current_token.upper() == "USING" or current_token.upper() == "ON" or current_token.upper() == "ORDER_BY" or current_token.upper() == "AND" or current_token.upper() == "OR"):
                        self.tokens.append(("KEYWORD", current_token))
                    elif inside_select_clause:
                        self.tokens.append(("COLUMN", current_token))
                    elif inside_from_clause:
                        self.tokens.append(("TABLE", current_token))
                    elif inside_join_clause:
                        self.tokens.append(("JOIN_VAR", current_token))
                    elif inside_on_clause:
                        self.tokens.append(("ON_VAR", current_token))
                    elif inside_using_clause:
                        self.tokens.append(("USING_VAR", current_token))
                    elif inside_where_clause:
                        self.tokens.append(("WHERE_VAR", current_token))
                    elif inside_order_by_clause:
                        self.tokens.append(("ORDER_BY_VAR", current_token))
                    elif current_token:
                        self.tokens.append(("UNDEFINED", current_token))

    def get_tokens(self):
        return self.tokens
