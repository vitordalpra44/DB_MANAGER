import sys
sys.path.append("../src/mysql")
import mysql_connection
import mysql_import_data

connection = mysql_connection.mysql_establish_connection('localhost', 'root', 'mudar', 'University')
mysql_import_data.saveTable('instructor', connection, 'University')
mysql_import_data.saveTable('teaches', connection, 'University')
mysql_import_data.saveTable('student', connection, 'University')
mysql_import_data.saveTable('department', connection, 'University')