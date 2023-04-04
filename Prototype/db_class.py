import sqlite3

class Database:
    def __init__(self):
      # Establishes database connection
      self.connection = sqlite3.connect("Prototype/cars.db")
      
      # Handles communication with database
      self.cursor = self.connection.cursor()
      
    def add_car(self, reg_no, score):
        self.cursor.execute("INSERT INTO cars VALUES (?, ?)", (reg_no, score))
      
        self.connection.commit()
    
        return
    
    def does_car_exist(self, reg_no):
        self.cursor.execute("SELECT * FROM cars WHERE registration_no=:reg", {"reg": reg_no})
        car_search = self.cursor.fetchone()
        
        print("Car Search", car_search)
        self.connection.commit()
                
        if car_search == None:
            return False
        return True
    
    def close_connection(self):
        self.connection.close()