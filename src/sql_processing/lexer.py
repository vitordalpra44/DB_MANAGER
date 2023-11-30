class Lexer:
    def __init__(self, query):
        self.query = query
        self.tokens = []
        self.type = ""




    def tokenize_select(self):
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

    def tokenize_delete(self):
        current_token = ""
        inside_delete_clause = False
        inside_join_clause = False
        inside_on_clause = False
        inside_where_clause = False
        inside_using_clause = False

        for char in self.query:
            if char.isalnum() or char == '_':
                current_token += char
            else:
                if current_token.upper() == "DELETE" or current_token.upper() == "FROM":
                    inside_delete_clause = True
                elif current_token.upper() == "JOIN":
                    inside_delete_clause = False
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
                    inside_delete_clause = False
                    inside_on_clause = False
                    inside_using_clause = False
                    inside_where_clause = True
                elif current_token == ";":
                    inside_delete_clause = False
                    inside_join_clause = False
                    inside_on_clause = False
                    inside_using_clause = False
                    inside_where_clause = False

                if char.isspace() or char in (',', ';', '(', ')', '*', '='):
                    if current_token and (current_token.upper() == "DELETE" or current_token.upper() == "FROM" or current_token.upper() == "JOIN" or current_token.upper() == "WHERE" or current_token.upper() == "USING" or current_token.upper() == "ON" or current_token.upper() == "AND" or current_token.upper() == "OR"):
                        self.tokens.append(("KEYWORD", current_token))
                    elif current_token and inside_delete_clause:
                        self.tokens.append(("TABLE", current_token))
                    elif current_token and inside_join_clause:
                        self.tokens.append(("JOIN_VAR", current_token))
                    elif current_token and inside_on_clause:
                        self.tokens.append(("ON_VAR", current_token))
                    elif current_token and inside_using_clause:
                        self.tokens.append(("USING_VAR", current_token))
                    elif current_token and inside_where_clause:
                        self.tokens.append(("WHERE_VAR", current_token))
                    elif current_token:
                        self.tokens.append(("UNDEFINED", current_token))
                    if char != ' ':
                        self.tokens.append((char, char))

                    current_token = ""
                

        if current_token:
                    if (current_token.upper() == "DELETE" or current_token.upper() == "FROM" or current_token.upper() == "JOIN" or current_token.upper() == "WHERE" or current_token.upper() == "USING" or current_token.upper() == "ON" or current_token.upper() == "AND" or current_token.upper() == "OR"):
                        self.tokens.append(("KEYWORD", current_token))
                    elif inside_delete_clause:
                        self.tokens.append(("TABLE", current_token))
                    elif inside_join_clause:
                        self.tokens.append(("JOIN_VAR", current_token))
                    elif inside_on_clause:
                        self.tokens.append(("ON_VAR", current_token))
                    elif inside_using_clause:
                        self.tokens.append(("USING_VAR", current_token))
                    elif inside_where_clause:
                        self.tokens.append(("WHERE_VAR", current_token))
                    else:
                        self.tokens.append(("UNDEFINED", current_token))

    def tokenize_insert(self):
        current_token = ""
        inside_insert_clause = False
        inside_name_column_clause = False
        inside_values_clause = False
        

        for char in self.query:
            if char.isalnum() or char == '_':
                current_token += char
            else:
                if current_token.upper() == "INSERT" or current_token.upper() == "INTO":
                    inside_insert_clause = True
                elif current_token == "(" and not inside_values_clause:
                    inside_name_column_clause = True
                    inside_insert_clause = False
                elif current_token.upper() == "VALUES":
                    inside_insert_clause = False
                    inside_name_column_clause = False
                    inside_values_clause = True
                elif current_token == ";":
                    inside_insert_clause = False
                    inside_name_column_clause = False
                    inside_values_clause = False

                if char.isspace() or char in (',', ';', '(', ')', '*', '='):
                    if current_token and (current_token.upper() == "INSERT" or current_token.upper() == "INTO" or current_token.upper() == "VALUES"):
                        self.tokens.append(("KEYWORD", current_token))
                    elif current_token and inside_insert_clause and not inside_name_column_clause:
                        self.tokens.append(("TABLE", current_token))
                    elif current_token and inside_name_column_clause:
                        self.tokens.append(("NAME_COLUMN", current_token))
                    elif current_token and inside_values_clause:
                        self.tokens.append(("VALUE_COLUMN", current_token))
                    elif current_token:
                        self.tokens.append(("UNDEFINED", current_token))
                    if char != ' ':
                        self.tokens.append((char, char))

                    current_token = ""
            if char == '(' and inside_insert_clause:
                inside_name_column_clause = True
                inside_insert_clause = False       

        if current_token:
                    if (current_token.upper() == "INSERT" or current_token.upper() == "INTO" or current_token.upper() == "VALUES"):
                        self.tokens.append(("KEYWORD", current_token))
                    elif inside_insert_clause and not inside_name_column_clause:
                        self.tokens.append(("TABLE", current_token))
                    elif inside_name_column_clause:
                        self.tokens.append(("NAME_COLUMN", current_token))
                    elif inside_values_clause:
                        self.tokens.append(("VALUE_COLUMN", current_token))
                    else:
                        self.tokens.append(("UNDEFINED", current_token))

    def tokenize(self):
        if "SELECT" in self.query.upper():
            self.tokenize_select()
            self.type="SELECT"
        elif "DELETE" in self.query.upper():
            self.tokenize_delete()
            self.type="DELETE"
        elif "INSERT" in self.query.upper():
            self.tokenize_insert()
            self.type="INSERT"
        else:
            print("Query is not parseable")

    def get_tokens(self):
        return self.tokens
