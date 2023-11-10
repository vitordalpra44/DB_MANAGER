import mysql.connector
import csv
import os

def saveTable(table, connection, database):
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM {table}")
    result = cursor.fetchall()
    
    with open(f"../databases/{database}/{table}.csv", 'w', newline='') as file_csv:
        writer_csv = csv.writer(file_csv)
        writer_csv.writerows(result)
    cursor.close()
