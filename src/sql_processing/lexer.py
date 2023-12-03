import keywords


class Lexer:
    def __init__(self, query):
        self.query = query
        self.tokens = []
        self.type = ""




    def tokenize_select(self):
        current_token = ""
        inside_join_clause = False
        inside_on_clause = False
        inside_where_clause = False
        inside_order_by_clause = False


        table_column = ("","")

        for char in self.query:
            if char.isalnum() or char == '_' or char =='.':
                current_token += char
            else:
                table_column = ("","")
                if '.' in current_token:
                    table_column = current_token.split('.')
                elif current_token.upper() == keywords.keyword_join:
                    inside_on_clause = False
                    inside_join_clause = True
                elif current_token.upper() == keywords.keyword_on:
                    inside_join_clause = False
                    inside_on_clause = True
                elif current_token.upper() == keywords.keyword_using:
                    inside_join_clause = False
                elif current_token.upper() == keywords.keyword_where:
                    inside_on_clause = False
                    inside_where_clause = True
                elif current_token.upper() == keywords.keyword_order_by:
                    inside_on_clause = False
                    inside_where_clause = False
                    inside_order_by_clause = True
                elif current_token == ";":
                    inside_join_clause = False
                    inside_on_clause = False
                    inside_where_clause = False
                    inside_order_by_clause = False

                if char.isspace() or char in (',', ';', '(', ')', '*', '=', '>', '<', '!'):
                    if current_token and (current_token.upper() in keywords.keywords):
                        self.tokens.append(("KEYWORD", current_token))
                    elif table_column[0] and table_column[1]:
                        self.tokens.append(("TABLE", table_column[0]))
                        self.tokens.append(("COLUMN", table_column[1]))
                    elif current_token and inside_join_clause:
                        self.tokens.append(("TABLE", current_token))
                    elif current_token and inside_on_clause:
                        self.tokens.append(("VALUE", current_token))
                    elif current_token and inside_where_clause:
                        self.tokens.append(("VALUE", current_token))
                    elif current_token and inside_order_by_clause:
                        self.tokens.append(("VALUE", current_token))
                    elif current_token:
                        self.tokens.append(("UNDEFINED", current_token))
                    if char != ' ':
                        if(char in ['>', '<', '=', '!']):
                            self.tokens.append(("OPERATION", char))
                        else:
                            self.tokens.append((char, char))

                    current_token = ""
                
                

        if current_token:
                    if  (current_token.upper() in keywords.keywords):
                        self.tokens.append(("KEYWORD", current_token))
                    elif table_column[0] and table_column[1]:
                        self.tokens.append(("TABLE", table_column[0]))
                        self.tokens.append(("COLUMN", table_column[1]))
                    elif  inside_join_clause:
                        self.tokens.append(("TABLE", current_token))
                    elif  inside_on_clause:
                        self.tokens.append(("VALUE", current_token))
                    elif  inside_where_clause:
                        self.tokens.append(("VALUE", current_token))
                    elif  inside_order_by_clause:
                        self.tokens.append(("VALUE", current_token))
                    elif current_token:
                        self.tokens.append(("UNDEFINED", current_token))

    def tokenize_delete(self):
        current_token = ""
        inside_delete_clause = False
        inside_join_clause = False
        inside_on_clause = False
        inside_where_clause = False


        table_column = ("","")
        for char in self.query:
            if char.isalnum() or char == '_' or char == '.':
                current_token += char
            else:
                table_column = ("","")
                if '.' in current_token:
                    table_column = current_token.split('.')
                elif current_token.upper() == keywords.keyword_delete_from:
                    inside_delete_clause = True
                elif current_token.upper() == keywords.keyword_join:
                    inside_delete_clause = False
                    inside_on_clause = False
                    inside_join_clause = True
                elif current_token.upper() == keywords.keyword_on:
                    inside_join_clause = False
                    inside_on_clause = True
                elif current_token.upper() == keywords.keyword_using:
                    inside_join_clause = False
                elif current_token.upper() == keywords.keyword_where:
                    inside_delete_clause = False
                    inside_on_clause = False
                    inside_where_clause = True
                elif current_token == ";":
                    inside_delete_clause = False
                    inside_join_clause = False
                    inside_on_clause = False
                    inside_where_clause = False

                if char.isspace() or char in (',', ';', '(', ')', '*', '=', '>', '<', '!'):
                    if current_token and (current_token.upper() in keywords.keywords):
                        self.tokens.append(("KEYWORD", current_token))
                    elif table_column[0] and table_column[1]:
                        self.tokens.append(("TABLE", table_column[0]))
                        self.tokens.append(("COLUMN", table_column[1]))
                    elif current_token and inside_delete_clause:
                        self.tokens.append(("TABLE", current_token))
                    elif current_token and inside_join_clause:
                        self.tokens.append(("TABLE", current_token))
                    elif current_token and inside_on_clause:
                        self.tokens.append(("VALUE", current_token))
                    elif current_token and inside_where_clause:
                        self.tokens.append(("VALUE", current_token))
                    elif current_token:
                        self.tokens.append(("UNDEFINED", current_token))
                    if char != ' ':
                        if(char in ['>', '<', '=', '!']):
                            self.tokens.append(("OPERATION", char))
                        else:
                            self.tokens.append((char, char))

                    current_token = ""
                

        if current_token:
                    if (current_token.upper() in keywords.keywords):
                        self.tokens.append(("KEYWORD", current_token))
                    elif table_column[0] and table_column[1]:
                        self.tokens.append(("TABLE", table_column[0]))
                        self.tokens.append(("COLUMN", table_column[1]))
                    elif inside_join_clause:
                        self.tokens.append(("TABLE", current_token))
                    elif inside_on_clause:
                        self.tokens.append(("VALUE", current_token))
                    elif inside_where_clause:
                        self.tokens.append(("VALUE", current_token))
                    elif current_token:
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
                if current_token.upper() == keywords.keyword_insert_into:
                    inside_insert_clause = True
                elif current_token == "(" and not inside_values_clause:
                    inside_name_column_clause = True
                    inside_insert_clause = False
                elif current_token.upper() == keywords.keyword_values:
                    inside_insert_clause = False
                    inside_name_column_clause = False
                    inside_values_clause = True
                elif current_token == ";":
                    inside_insert_clause = False
                    inside_name_column_clause = False
                    inside_values_clause = False

                if char.isspace() or char in (',', ';', '(', ')', '*', '=', '>', '<', '!'):
                    if current_token and (current_token.upper() in keywords.keywords):
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
                        if char == '(':
                            self.tokens.append(("NEW_VALUE", char))
                        else:
                            self.tokens.append((char, char))

                    current_token = ""
            if char == '(' and inside_insert_clause:
                
                inside_name_column_clause = True
                inside_insert_clause = False       

        if current_token:
                    if (current_token.upper() in keywords.keywords):
                        self.tokens.append(("KEYWORD", current_token))
                    elif inside_insert_clause and not inside_name_column_clause:
                        self.tokens.append(("TABLE", current_token))
                    elif inside_name_column_clause:
                        self.tokens.append(("NAME_COLUMN", current_token))
                    elif inside_values_clause:
                        self.tokens.append(("VALUE_COLUMN", current_token))
                    else:
                        self.tokens.append(("UNDEFINED", current_token))



    def tokenize_update(self):
        current_token = ""
        inside_update_clause = False
        inside_where_clause = False
        inside_set_clause = False
        inside_column_clause = False

        table_column = ("","")
        for char in self.query:
            if char.isalnum() or char == '_' or char == '.':
                current_token += char
            else:
                table_column = ("","")
                if '.' in current_token:
                    table_column = current_token.split('.')
                elif current_token.upper() == keywords.keyword_update:
                    inside_update_clause = True
                elif current_token.upper() == keywords.keyword_where:
                    inside_update_clause = False
                    inside_where_clause = True
                    inside_column_clause = False
                    inside_set_clause = False

                elif current_token.upper() == keywords.keyword_set:
                    inside_update_clause = False
                    inside_where_clause = False
                    inside_set_clause = True
                elif current_token.upper() == "=" and inside_set_clause:
                    inside_update_clause = False
                    inside_where_clause = False
                    inside_set_clause = False
                    inside_column_clause = True
                elif current_token == ";":
                    inside_update_clause = False
                    inside_where_clause = False

                if char.isspace() or char in (',', ';', '(', ')', '*', '=', '>', '<', '!'):
                    if current_token and (current_token.upper() in keywords.keywords):
                        self.tokens.append(("KEYWORD", current_token))
                    elif table_column[0] and table_column[1]:
                        self.tokens.append(("TABLE", table_column[0]))
                        self.tokens.append(("COLUMN", table_column[1]))
                    elif current_token and inside_update_clause:
                        self.tokens.append(("TABLE", current_token))
                    elif current_token and inside_where_clause:
                        self.tokens.append(("VALUE", current_token))
                    elif current_token and inside_column_clause:
                        self.tokens.append(("VALUE", current_token))
                    elif current_token and inside_set_clause:
                        self.tokens.append(("COLUMN", current_token))
                    elif current_token:
                        self.tokens.append(("UNDEFINED", current_token))
                    if char != ' ':
                        if(char in ['>', '<', '=', '!']):
                            self.tokens.append(("OPERATION", char))
                        else:
                            self.tokens.append((char, char))

                    current_token = ""
                

        if current_token:
                    if  (current_token.upper() in keywords.keywords):
                        self.tokens.append(("KEYWORD", current_token))
                    elif table_column[0] and table_column[1]:
                        self.tokens.append(("TABLE", table_column[0]))
                        self.tokens.append(("COLUMN", table_column[1]))
                    elif  inside_update_clause:
                        self.tokens.append(("TABLE", current_token))
                    elif  inside_where_clause:
                        self.tokens.append(("VALUE", current_token))
                    elif  inside_column_clause:
                        self.tokens.append(("VALUE", current_token))
                    elif  inside_set_clause:
                        self.tokens.append(("COLUMN", current_token))
                    elif current_token:
                        self.tokens.append(("UNDEFINED", current_token))

    def tokenize(self):
        if keywords.keyword_select in self.query.upper():
            self.tokenize_select()
            self.type=keywords.keyword_select
        elif keywords.keyword_delete_from in self.query.upper():
            self.tokenize_delete()
            self.type=keywords.keyword_delete_from
        elif keywords.keyword_insert_into in self.query.upper():
            self.tokenize_insert()
            self.type=keywords.keyword_insert_into
        elif keywords.keyword_update in self.query.upper():
            self.tokenize_update()
            self.type=keywords.keyword_update
        else:
            print("Query is not parseable")

    def get_tokens(self):
        return self.tokens
