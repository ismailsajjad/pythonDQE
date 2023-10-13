# SQLite3
# ODBC open database connectivity
#
import sqlite3
import pyodbc
# connection = sqlite3.connect('10test.db')
# cursor = connection.cursor()
#
# cursor.execute('CREATE TABLE IF NOT EXISTS  people (firstname text, lastname text, age real)')
# cursor.execute("INSERT INTO people VALUES('Ismail', 'sajjad', 34)")
# cursor.execute("INSERT INTO people VALUES('Muhammad', 'ismail', .5)")
# cursor.execute('select * from people')
# result = cursor.fetchall()
# print(result)
# print(type(result))
# print(type(result[0]))
# print(result[0])
# print(result[0][0])
# connection.commit()
# connection.close()

#
# with sqlite3.connect('10test.db') as connection:
#     cursor = connection.cursor()
#     cursor.execute("INSERT INTO people VALUES('Sajjad', 'Hussain', 55)")
#     cursor.execute("INSERT INTO people VALUES('Ismail', 'sajjad', 34)")
#     cursor.execute("INSERT INTO people VALUES('Muhammad', 'ismail', .5)")
#     cursor.execute('select * from people')
#     result = cursor.fetchall()
#     print(result)

print("aaa")
connection  = pyodbc.connect('Driver={SQLite3 ODBC Driver};'
                             'Direct=True;'
                             'Database=10test.db'
                             ,autocommit=True
                             )
cursor = connection.cursor()


