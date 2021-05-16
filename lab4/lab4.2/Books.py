import wx
import sqlite3

DBname = r'library.db'
db = sqlite3.connect(DBname)


def sql_connection():
    try:

        con = sqlite3.connect('library.db')

        return con

    except Error:

        print(Error)


def table(con):
    cursor = con.cursor()
    s = 'id Автора  - Название - Количество страниц - Издательство - Год издания\n'
    for value in cursor.execute("SELECT * FROM books"):
        s = +str(value[0]) + str(value[1]) + str(value[2]) + str(value[3]) + str(value[4]) + '\n'
    return s
    con.commit()


con = sql_connection()


class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, title=title)
        self.SetSize((500, 400))

        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)

        vbox.Add((wx.StaticText(panel, label="Все книги:")), flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.BOTTOM)
        tb = wx.TextCtrl(panel, style=wx.TE_MULTILINE | wx.TE_READONLY | wx.HSCROLL | wx.TE_RICH)
        self.tb = tb
        vbox.Add(tb, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.BOTTOM, border=15, proportion=1)
        self.tb.AppendText(table(con))
        panel.SetSizer(vbox)


app = wx.App()
wnd = MyFrame(None, 'Kravchenko Alina Exercise 2')
wnd.Show(True)
app.MainLoop()