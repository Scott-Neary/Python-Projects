import sqlite3

class Database:
    def __init__(self, name):
      self.name = name
    
    def add_car():
        insert_car_query = ("INSERT INTO cars VALUES (:reg, :veh_status, :path)", {'reg': reg_no, 'veh_status': status, 'path': img_path})
        
    def delete_car():
        tmp = ""

    def does_car_exist():
        car_exist_query = ("SELECT * FROM cars WHERE registration_no=:r", {"r": reg_no})
        
        if car_exist_query == "":
            return False
        return True
        
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

val = "NK16VEX"

# Print specific rows
print("***************************")
cursor.execute("select * from cars where registration_no=:r", {"r": val})
car_search = cursor.fetchone()
print("Result - ", car_search)

# print("***************************")
# cursor.execute("create table cardesc (car_reg text, car_colour text)")
# cursor.execute("insert into cardesc values (?,?)", ("SD14NMA", "Blue"))
# cursor.execute("select * from cardesc where car_colour=:c", {"c": "Blue"})
# cardesc_search = cursor.fetchall()
# print(cardesc_search)

# Manipulate database
# print("***************************")
# for i in car_search:
#     adjusted = [cardesc_search[0][1] if value ==cardesc_search[0][0] else value for value in i]
#     print(adjusted)
     
connection.close()