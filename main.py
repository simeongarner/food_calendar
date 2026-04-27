from app import App

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
    
<<<<<<< HEAD
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
=======
>>>>>>> 717ecf55500bb788a2c5e566a71a944a77f01fd9

def main():
    app = App()

<<<<<<< HEAD
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

=======
    app.mainloop()

if __name__ == "__main__":
    main()
>>>>>>> 717ecf55500bb788a2c5e566a71a944a77f01fd9
