import requests
import sqlite3

connection = sqlite3.connect("jobs.db")
cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS job (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT UNIQUE, image TEXT)")

query_string = "INSERT INTO job (name, image) VALUES ('{}', '{}')".format("test1", "redis/redis:latest")
returned = cursor.execute(query_string).fetchall()
print(returned)


query_string = "INSERT INTO job (name, image) VALUES ('{}', '{}')".format("test2", "redis/redis1:latest")
cursor.execute(query_string)


#rows = cursor.execute("SELECT * FROM job").fetchall()
row = cursor.execute('SELECT * FROM job WHERE name = "test2"').fetchall()
print(row)