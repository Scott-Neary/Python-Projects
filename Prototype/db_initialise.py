import sqlite3

connection = sqlite3.connect("Prototype/cars.db")

# Handles communication with database
cursor = connection.cursor()

# Create table and fields
cursor.execute("""CREATE TABLE cars (
                registration_no text, 
                accuracy_score text
                )""")

# Sample data
release_list = [
    ("SD14NMA", "0.58"),
    ("NK16VEX", "0.72")
]

# Insert data into table
cursor.executemany("insert into cars values (?,?)", release_list)

# Print data
for row in cursor.execute("select * from cars"):
    print(row)

# Close database connection    
connection.close()