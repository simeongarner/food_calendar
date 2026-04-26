import tkinter as tk
from database import Database
from constants import *
import calendar
from datetime import date

class DayCard(tk.Frame):
    @property
    def bg(self):
        return self.cget("bg")

    def __init__(self, meal: str, day: str, *args, **kwargs):
        super().__init__(*args, **kwargs, width=Button.width, height=Button.height, bg=Button.color, borderwidth=Button.borderWidth, relief=Button.relief)
        self.meal = meal
        self.day = day
        
        self.dayLabel = tk.Label(master=self, text=day, bg=self.bg)
        self.mealLabel = tk.Label(master=self, text=meal, bg=self.bg)

        self.bind_button(Button.click, self.onClick)
        self.bind_button(Button.release, self.onRelease)

        self.dayLabel.pack(side="top", anchor="nw")
        self.mealLabel.pack(side="bottom", anchor="s")

        self.pack_propagate(False)

    def bind_button(self, click_type, callback):
        self.dayLabel.bind(click_type, callback)
        self.mealLabel.bind(click_type, callback)
        self.bind(click_type, callback)

    def onClick(self, *args):
        self.config(bg=Button.colorPressed, relief=Button.reliefPressed)
        self.dayLabel.config(bg=Button.colorPressed)
        self.mealLabel.config(bg=Button.colorPressed)

    def onRelease(self, *args):
        self.config(bg=Button.color, relief=Button.relief)
        self.dayLabel.config(bg=Button.color)
        self.mealLabel.config(bg=Button.color)

    def grid(self, *args, **kwargs):
        super().grid(*args, **kwargs, padx=Button.pad, pady=Button.pad)

class App(tk.Tk):
    def __init__(self, screenName = None, baseName = None, className = "Tk", useTk = True, sync = False, use = None):
        super().__init__(screenName, baseName, className, useTk, sync, use)

        self.title(AppConfig.title)
        self.iconphoto(False, tk.PhotoImage(file=AppConfig.ico))
        self.cards = []

        self.date = date.today()

        startDay = self.getStartDayOfWeek()
        daysInMonth = self.getMonthDays(self.date.month)

        r = 0
        for i in range(startDay, daysInMonth):
            if i % 7 == 0:
                r += 1
            card = DayCard("Meal", master=self, day=calendar.day_name[i % 7])
            card.grid(row=r, column=i % 7)
            self.cards.append(card)

        self.db = Database()

    # TODO: Implement: Calculate the number of days for a given month (by month number ex. January = 1)
    def getMonthDays(self, month) -> int:
        return 30

    # TODO: Implement: Calculate the day of the week that the beginning of the month will start on
    def getStartDayOfWeek(self) -> int:
        return calendar.MONDAY

    # TODO: Implement: Calculate if the year is a leap year or not, return True (is a leap year) or False (not a leap year)
    def isLeapYear(self, year) -> bool:
        pass