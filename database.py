import sqlite3

conn = sqlite3.connect('users.db')
c = conn.cursor()

# Crear tabla de usuarios
c.execute('''
          CREATE TABLE IF NOT EXISTS users
          (id INTEGER PRIMARY KEY, 
          username TEXT UNIQUE, 
          password TEXT)
          ''')
conn.commit()
conn.close()
