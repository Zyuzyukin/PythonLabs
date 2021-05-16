import sqlite3

from sqlite3 import Error

DBname =r'library.db'
db =sqlite3.connect(DBname)


def sql_connection():

    try:

        con = sqlite3.connect('library.db')

        return con

    except Error:

        print(Error)

def sql_table(con):

    cursorObj = con.cursor()

    cursorObj.execute("INSERT INTO author (id, name, country,life) VALUES (?,?,?,?); " ,( 1 ,'Пушкин' ,'Росия' ,36))
    con.commit()

con = sql_connection()
sql_table(con)