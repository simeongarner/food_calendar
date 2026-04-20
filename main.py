import sqlite3
import tkinter as tk
import os

DATABASE = "./food.db"

# TODO: 1. Create Database
'''
    Needed functions:
        - Get meal
        - Add meal
''' 


# TODO: Create GUI
# TODO: 2. Create layout
# -------------------------------------------------------------------
# |   -------  -------  -------  -------  -------  -------  ------- |
# |   |   1 |  |   2 |  |   3 |  |   4 |  |   5 |  |   6 |  |   7 | |
# |   | Meal|  | Meal|  | Meal|  | Meal|  | Meal|  | Meal|  | Meal| |
# |   -------  -------  -------  -------  -------  -------  ------- |
# -------------------------------------------------------------------
# |   -------  -------  -------  -------  -------  -------  ------- |
# |   |     |  |     |  |     |  |     |  |     |  |     |  |     | |
# |   |     |  |     |  |     |  |     |  |     |  |     |  |     | |
# |   -------  -------  -------  -------  -------  -------  ------- |
# -------------------------------------------------------------------
# |   -------  -------  -------  -------  -------  -------  ------- |
# |   |     |  |     |  |     |  |     |  |     |  |     |  |     | |
# |   |     |  |     |  |     |  |     |  |     |  |     |  |     | |
# |   -------  -------  -------  -------  -------  -------  ------- |
# -------------------------------------------------------------------
# |   -------  -------  -------  -------  -------  -------  ------- |
# |   |     |  |     |  |     |  |     |  |     |  |     |  |     | |
# |   |     |  |     |  |     |  |     |  |     |  |     |  |     | |
# |   -------  -------  -------  -------  -------  -------  ------- |
# -------------------------------------------------------------------

class DayCard(tk.Frame):
    def __init__(self, meal, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.meal = meal
        self.bind("<Button-1>", self.onClick)

    def onClick(self, *args):
        print("Clicked")

class MealsTable:
    id = "id"
    name = "meals"

class DBTypes:
    integer = "INTEGER"
    text = "text"

class DBConstraints:
    primaryKey = "PRIMARY KEY"
    notNull = "NOT NULL"

class Database:
    def __init__(self):
        if not os.path.exists(DATABASE):
            with open(DATABASE, "w") as f:
                pass

        self.connection = sqlite3.connect(DATABASE)
        self.create_meals_table()
      
    def create_meals_table(self):
        table_args = ""
        table_args += self.create_column_string(MealsTable.id, DBTypes.integer, DBConstraints.primaryKey)
        table_args += self.create_column_string(MealsTable.name, DBTypes.text, DBConstraints.notNull)

        self.create_table("meals", table_args)

    def create_column_string(self, name, datatype, constraint):
        return f"{name} {datatype} {constraint},"

    def create_table(self, table, table_args):
        self.connection.cursor().execute(f"CREATE TABLE IF NOT EXISTS {table} ({table_args});")

def connect_db():
    

    connection = sqlite3.connect(DATABASE)

    connection.cursor().execute(CREATE_TABLE)
    connection.commit()

    connection.cursor().execute("INSERT INTO meals (id, name) values(1, 'Lasagna')")
    connection.commit()

    meals = connection.cursor().execute("SELECT * FROM meals")
    
    for meal in meals:
        print("Found meal:", meal)

    return connection
    

def main():
    db = connect_db()
    # app = tk.Tk()
    # app.title("Food Calendar")
    # app.geometry("350x200")
    # app.iconphoto(False, tk.PhotoImage(file="apple.ico"))
    # card = DayCard("Meal", master=app, width=100, height=100, bg="blue")
    # card.pack()

    # app.mainloop()
    db.close()


if __name__ == "__main__":
    main()
     

