import wx
import sqlite3

ID_BUT = 1
DBname = r'library.db'
db = sqlite3.connect(DBname)


def sql_connection():
    try:

        con = sqlite3.connect('library.db')

        return con

    except Error:

        print(Error)


def addBook(con, title, pages, publisher, year_publishing):
    cursor = con.cursor()
    i = 0
    for value in cursor.execute("SELECT * FROM books"):
        print(value)
        i = +1
    cursor.execute("INSERT INTO books (id_author,title,pages,publishing,year_publishing) VALUES (?,?, ?,?,?);",
                   (i + 1, title, pages, publisher, year_publishing))

    con.commit()


con = sql_connection()


class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, title=title)
        self.SetSize((500, 400))

        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add((wx.StaticText(panel, label="")), flag=wx.EXPAND | wx.LEFT | wx.RIGHT)
        vbox.Add((wx.StaticText(panel, label="Название:")), flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=20)
        tbt = wx.TextCtrl(panel, style=wx.HSCROLL | wx.TE_RICH)
        self.tbt = tbt
        vbox.Add(tbt, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.BOTTOM, border=10)

        vbox.Add((wx.StaticText(panel, label="")), flag=wx.EXPAND | wx.LEFT | wx.RIGHT)
        vbox.Add((wx.StaticText(panel, label="Количество страниц:")), flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=20)
        tbs = wx.TextCtrl(panel, style=wx.HSCROLL | wx.TE_RICH)
        self.tbs = tbs
        vbox.Add(tbs, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.BOTTOM, border=10)

        vbox.Add((wx.StaticText(panel, label="")), flag=wx.EXPAND | wx.LEFT | wx.RIGHT)
        vbox.Add((wx.StaticText(panel, label="Издательство:")), flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=20)
        tbi = wx.TextCtrl(panel, style=wx.HSCROLL | wx.TE_RICH)
        self.tbi = tbi
        vbox.Add(tbi, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.BOTTOM, border=10)

        vbox.Add((wx.StaticText(panel, label="")), flag=wx.EXPAND | wx.LEFT | wx.RIGHT)
        vbox.Add((wx.StaticText(panel, label="Год издания:")), flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=20)
        tby = wx.TextCtrl(panel, style=wx.HSCROLL | wx.TE_RICH)
        self.tby = tby
        vbox.Add(tby, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.BOTTOM, border=10)

        button = wx.Button(panel, label="Добавить", id=ID_BUT)
        self.button = button
        vbox.Add(self.button, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.BOTTOM, border=10, proportion=1)

        panel.SetSizer(vbox)
        self.Bind(wx.EVT_BUTTON, self.add, id=ID_BUT)

    def add(self, event):
        title = self.tbt.GetValue()
        pages = self.tbs.GetValue()
        publisher = self.tbi.GetValue()
        year_publishing = self.tby.GetValue()
        addBook(con, title, pages, publisher, year_publishing)


app = wx.App()
wnd = MyFrame(None, 'Kravchenko Alina Exercise 2')
wnd.Show(True)
app.MainLoop()
