import mysql.connector
db = mysql.connector.connect(
	host = 'localhost',
	user = 'root',
	password = 'root',
	)
cursor = db.cursor()
cursor.execute("CREATE DATABASE yash123")
print("Doneeee!")