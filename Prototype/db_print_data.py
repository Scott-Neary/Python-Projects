import sqlite3

connection = sqlite3.connect("Prototype/cars.db")

# Handles communication with database
cursor = connection.cursor()

# Print data
for row in cursor.execute("select * from cars"):
    print(row)

# Close database connection    
connection.close()