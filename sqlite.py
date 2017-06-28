import sqlite3
import os

conn = sqlite3.connect(os.path.dirname(os.path.realpath(__file__)) + '\\test.db')

print ("Opened database successfully");

cursor = conn.execute('SELECT max(id) FROM test')
# print(cursor.fetchall())
for row in cursor:
  print(row)

exit()

while True:
    word = input ('Bitte gib mir nur ein Wort:')
    if word == '':
        break
    else:
        conn.execute('INSERT INTO test(id, data) VALUES (?,?)', (2,'test'))

cursor = conn.execute('SELECT * FROM test')
# print(cursor.fetchall())
for row in cursor:
  print(row)

conn.close()