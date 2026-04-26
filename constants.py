from dataclasses import dataclass
from tkinter import RAISED, FLAT

@dataclass(frozen=True)
class AppConfig:
    title = "Food Calendar"
    ico = "apple.ico"

DATABASE = "./food.db"

@dataclass(frozen=True)
class Button:
    click = "<Button-1>"
    release = "<ButtonRelease-1>"
    color = "white"
    colorPressed = "green"
    width = 150
    height = width
    borderWidth = 1
    relief = RAISED
    reliefPressed = FLAT
    pad = 1

@dataclass(frozen=True)
class Table:
    id = "id"

@dataclass(frozen=True)
class MealsTable(Table):
    name = "meals"

@dataclass(frozen=True)
class DBTypes:
    integer = "INTEGER"
    text = "text"

@dataclass(frozen=True)
class DBAttr:
    primaryKey = "PRIMARY KEY"
    notNull = "NOT NULL"