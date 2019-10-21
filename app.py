import sqlite3

# Create Database
conn = sqlite3.connect('mammals.db')

# Create Cursor
cur = conn.cursor()

#Create Table Structure
# cur.execute("""CREATE TABLE domestic(
#     habitat text,
#     foodprefs text,
#     max_age integer
#     )""")

# Add Data
cur.execute("INSERT INTO domestic VALUES ('Bedroom', 'herbivore', 14) ")

conn.commit()

# Read From Database
cur.execute("SELECT * FROM domestic WHERE max_age = 14")

# Print Results of Query
print(cur.fetchall())

conn.commit()

conn.close()