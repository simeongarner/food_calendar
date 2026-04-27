# TODO: 1. Create Database
# '''
#     Needed functions:
#         - Get meal
#         - Add meal
# ''' 
# TODO: 2. Create GUI
# TODO: 3. Create layout
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


#_____________________________CLASSES_______________________________|
# class MealsTable:
#     id = "id"
#     name = "meals"

# class DBTypes:
#     integer = "INTEGER"
#     text = "text"

# class DBConstraints:
#     primaryKey = "PRIMARY KEY"
#     notNull = "NOT NULL"

# class DayCard(tk.Frame):3
#     def __init__(self, meal, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.meal = meal
#         self.bind("<Button-1>", self.onClick)

#     def onClick(self, *args):
#         print("Clicked")

# class Database:
#     def __init__(self):
#         if not os.path.exists(DATABASE):
#             with open(DATABASE, "w") as f:
#                 pass

#         self.connection = sqlite3.connect(DATABASE)
#         self.create_meals_table()
      
#     def create_meals_table(self):
#         table_args = ""
#         table_args += self.create_column_string(MealsTable.id, DBTypes.integer, DBConstraints.primaryKey)
#         table_args += self.create_column_string(MealsTable.name, DBTypes.text, DBConstraints.notNull)

#         self.create_table("meals", table_args)

#     def create_column_string(self, name, datatype, constraint):
#         return f"{name} {datatype} {constraint},"

#     def create_table(self, table, table_args):
#         self.connection.cursor().execute(f"CREATE TABLE IF NOT EXISTS {table} ({table_args});")

# def connect_db():
    
#     connection = sqlite3.connect(DATABASE)

#     connection.cursor().execute(CREATE_TABLE)
#     connection.commit()

#     connection.cursor().execute("INSERT INTO meals (id, name) values(1, 'Lasagna')")
#     connection.commit()

#     meals = connection.cursor().execute("SELECT * FROM meals")
    
#     for meal in meals:
#         print("Found meal:", meal)

#     return connection

#_____________________________IMPORTS_______________________________|
import sqlite3
import tkinter as tk
import os
from tkinter import ttk, messagebox
import calendar
from datetime import datetime

#____________________________VARIABLES______________________________|
DATABASE = "./food.db"

#___________________________COLOR-THEME_____________________________|
COLORS = {
    "bg": "#FFFFFF",#Background color
    "header_bg": "#0D265C",#Header color
    "header_fg": "#0D265C",#Changed from black - TEXT color
    "footer_fg": "#0D265C", 
}    
#___________________________________________________________________|

def main():
    # db = connect_db()
    app = tk.Tk()
    app.title("Food Calendar")
    app.geometry("1366x768")
    app.iconphoto(False, tk.PhotoImage(file="apple.ico"))
    app.configure(bg="#0D265C")#this 
    # card = DayCard("Meal", master=app, width=100, height=100, bg="blue")
    # card.pack()

    header_frame = tk.Frame(app, bg=COLORS["header_bg"], pady=12)
    header_frame.pack(fill="x")
    
    dow_frame = tk.Frame(app, bg=COLORS["header_bg"])
    dow_frame.pack(fill="x")
    
    day_names = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    for d in day_names:
        lbl = tk.Label(dow_frame, text=d, font=("Helvetica", 11, "bold"),
                       bg=COLORS["header_bg"], fg="#ffffff",
                       width=15, anchor="center", pady=6)
        lbl.pack(side="left", expand=True, fill="x")
    
    app.mainloop()#This is an infinite loop that keeps the app open 
    # db.close()

if __name__ == "__main__":
    main()

