import sqlite3

connection = sqlite3.connect("Prototype/cars.db")

# Handles communication with database
cursor = connection.cursor()

# Create table and fields
cursor.execute("""CREATE TABLE cars (
                registration_no text, 
                status text, 
                image_path text
                )""")

release_list = [
    ("SD14NMA", "Employee", "Prototype/Images/frame240.jpg"),
    ("NK16VEX", "Blacklist", "Prototype/Images/car0.jpg")
]

# Insert data into table
cursor.executemany("insert into cars values (?,?,?)", release_list)

# Print data
for row in cursor.execute("select * from cars"):
    print(row)

# Close database connection    
connection.close()