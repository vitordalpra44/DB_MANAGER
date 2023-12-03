import mysql.connector
import csv
import os

def saveTable(table, connection, database):
        cursor = connection.cursor()

        cursor.execute(f"DESCRIBE {table}")
        schema_info = cursor.fetchall()


        field_lines = [f"{table}-{column_info[0]}-{column_info[1].decode('utf-8')}"
                        if isinstance(column_info[1], bytes)
                        else f"{column_info[0]}-{column_info[1]}-{column_info[2]}"
                        for column_info in schema_info]
        
        cursor.execute(f"SELECT * FROM {table}")
        result = cursor.fetchall()


        with open(f"../databases/{database}/{table}.csv", 'w', newline='') as file_csv:
                writer_csv = csv.writer(file_csv, delimiter=';')
                writer_csv.writerow(field_lines)
                print(field_lines)
                writer_csv.writerows(result)

        cursor.close()

