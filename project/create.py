import sqlite3
from data import data

# Connect to a new database
conn = sqlite3.connect('project_database.db')

# Create a new table using the DDL
conn.execute('''CREATE TABLE ingredients (
                 name VARCHAR(50) PRIMARY KEY,
                 fat INT NOT NULL,
                 calories INT NOT NULL,
                 proteins INT NOT NULL,
                 qty_gram INT DEFAULT 100
               )''')

conn.executemany("INSERT INTO ingredients (name, fat, calories, proteins) VALUES (?, ?, ?, ?)", data)
conn.commit()
conn.close()

print("Table created and data inserted successfully!")