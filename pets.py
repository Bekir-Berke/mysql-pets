import mysql.connector
from mysql.connector import Error

#Database connection
connection = mysql.connector.connect(host='',
                                         database='',
                                         user='',
                                         password='')
if connection.is_connected():
    print('Connected to MySQL database')

# Fetch all cats from table
def fetchCats():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM cats")
    result = cursor.fetchall()
    for x in result:
        print(x)
fetchCats()

# Fetch cat by owner
def fetchCatByOwner():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM cats WHERE owner = 'Casey'")
    result = cursor.fetchall()
    print(result)
fetchCatByOwner()

# Fetch cat by id
def fetchCatById():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM cats WHERE id = '1'")
    result = cursor.fetchall()
    print(result)
fetchCatById()