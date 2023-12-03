import sys
sys.path.append("../src/mysql")
import mysql_connection
import mysql_import_data

connection = mysql_connection.mysql_establish_connection('localhost', 'root', 'mudarasenha', 'University')
mysql_import_data.saveTable('instructor', connection, 'University')