import sqlite3

class Database:
    def __init__(self):
      # Establishes database connection
      self.connection = sqlite3.connect("Prototype/cars.db")
      
      # Handles communication with database
      self.cursor = self.connection.cursor()
      
    def add_car(self, reg_no, status, img_path):
        self.cursor.execute("INSERT INTO cars VALUES (?, ?, ?)", (reg_no, status, img_path))
      
        self.connection.commit()
        
        # Print data
        for row in self.cursor.execute("select * from cars"):
            print(row)
    
        self.connection.close()
        return
    
    def does_car_exist(self, reg_no):
        car_exist_query = ("SELECT * FROM cars WHERE registration_no=:reg", {"reg": reg_no})
        
        self.connection.close()
        
        if car_exist_query == "":
            return False
        return True