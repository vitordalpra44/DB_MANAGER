#This code establishes a connection to a mysql database.
import mysql.connector
import os

def mysql_establish_connection(host, user, password, database):
    #Connecting to mysql
    connection = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )

    #ok?
    if connection.is_connected():
        print("Connection Established!")
        if not os.path.exists(f"../databases/{database}"):
            os.makedirs(f"../databases/{database}")
            print(f"Diretório criado: ../databases/{database}")
            with open(f"../databases/{database}/ignore", 'w') as ignore_file:
                ignore_file.write("ignore")
        else:
            print(f"Diretório já existe: ../databases/{database}")

    else:
        print("Connection Failed!")
    return connection


