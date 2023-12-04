from pathlib import Path
import sys
import os
sys.path.append("../src/sql_processing")
sys.path.append("../src/mysql")
import global_var
from tree_func import *
from mysql_import_data import *
from mysql_connection import *
import getpass

mode = 0
while(mode != '4'):
    
    print("1 - Listar tabelas")
    print("2 - Conectar a database")
    print("3 - Extrair do MySQL")
    print("4 - Sair")
    mode = input("Selecione a opção:")

    if (mode == '1'):
        directory_path = Path("../databases")

        items = directory_path.iterdir()

        dbs = [item for item in items if item.is_dir()]

        print("Databases:\n", [db.name for db in dbs])


    if (mode == '2'):
        global_var.database = input("database -> ")
        query = None
        while(True):
            query = input(f"query ({global_var.database}) -> ")
            if query == "exit":
                break
            table = tree_operation(query)
            if(table == -1):
                print("query realizada!")
            elif (table):
                for row in table:
                    print(row)
            else:
                print("")

    if (mode == '3'):
        host = input("Host:")
        username = input("Username: ")
        password = getpass.getpass("Senha: ")
        s_db = input("Database desejada: ")
        s_table = input("Tabela: ")
        
        connection = mysql_establish_connection(host, username, password, s_db)
        saveTable(s_db, connection, s_db)
        
    if (mode == '4'):
        break