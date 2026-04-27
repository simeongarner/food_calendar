import sqlite3
import pandas as pd
from os.path import exists
from constants import *

class Database:
    def __init__(self):
        if not exists(DATABASE):
            with open(DATABASE, "w") as f:
                pass

        self.connection = sqlite3.connect(DATABASE)
        self.create_meals_table()
      
    def create_meals_table(self):
        table_args = ""
        table_args += self.create_column_string(MealsTable.id, DBTypes.integer, DBAttr.primaryKey)
        table_args += self.create_column_string(MealsTable.name, DBTypes.text, DBAttr.notNull)

        table_args = table_args[0:-1]
        self.create_table("meals", table_args)

    def create_column_string(self, name, datatype, constraint):
        return f"{name} {datatype} {constraint},"

    def create_table(self, table, table_args):
        self.connection.cursor().execute(f"CREATE TABLE IF NOT EXISTS {table} ({table_args});")

    def get_meals_table(self) -> pd.DataFrame:
        return self.get_table("meals")

    def get_table(self, table) -> pd.DataFrame: 
        return pd.read_sql_table(table_name=table, con=self.connection)

    def close(self):
        self.connection.close()