from pathlib import Path
import global_var

mode = 0
while(mode != '4'):

    print("Selecione a opção:")
    print("1 - Listar tabelas")
    print("2 - Conectar a database")
    print("3 - Extrair do SQL\n")

    print("4 - Sair\n")

    mode = input()

    if (mode == '1'):
        directory_path = Path("..\databases")

        items = directory_path.iterdir()

        dbs = [item for item in items if item.is_dir()]

        print("Databases:\n", [str(db) for db in dbs], "\n\n")


    if (mode == '2'):
        global_var.database = input("Database: ")
        query = None
        while(query != 'exit'):
            query = input()



    if (mode == '3'):
        host = input("Host:")
        username = input("Username: ")
        password = input("Senha: ")
        s_db = input("Database desejada: ")
        s_table = input("Tabela: ")



    if (mode == '4'):
        break