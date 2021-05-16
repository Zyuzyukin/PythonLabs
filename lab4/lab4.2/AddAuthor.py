import xml.etree.ElementTree as ET
import wx
import sqlite3

ID_BUT = 1
ID_BUTR = 1
DBname = r'library.db'
db = sqlite3.connect(DBname)


def sql_connection():
    try:

        con = sqlite3.connect('library.db')

        return con

    except Error:

        print(Error)


def addAuthor(con, name, country, life):
    cursor = con.cursor()
    i = 0
    for value in cursor.execute("SELECT * FROM author"):
        print(value)
        i = +1
    cursor.execute("INSERT INTO author (id, name, country,life) VALUES (?,?, ?,?);", (i + 1, name, country, life))

    con.commit()


con = sql_connection()


class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, title=title)
        self.SetSize((500, 400))

        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add((wx.StaticText(panel, label="")), flag=wx.EXPAND | wx.LEFT | wx.RIGHT)
        vbox.Add((wx.StaticText(panel, label="Имя:")), flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=20)
        tbt = wx.TextCtrl(panel, style=wx.HSCROLL | wx.TE_RICH)
        self.tbt = tbt
        vbox.Add(tbt, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.BOTTOM, border=10)

        vbox.Add((wx.StaticText(panel, label="")), flag=wx.EXPAND | wx.LEFT | wx.RIGHT)
        vbox.Add((wx.StaticText(panel, label="Страна:")), flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=20)
        tbs = wx.TextCtrl(panel, style=wx.HSCROLL | wx.TE_RICH)
        self.tbs = tbs
        vbox.Add(tbs, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.BOTTOM, border=10)

        vbox.Add((wx.StaticText(panel, label="")), flag=wx.EXPAND | wx.LEFT | wx.RIGHT)
        vbox.Add((wx.StaticText(panel, label="Года жизни:")), flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=20)
        tbi = wx.TextCtrl(panel, style=wx.HSCROLL | wx.TE_RICH)
        self.tbi = tbi
        vbox.Add(tbi, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.BOTTOM, border=10)

        hbox = wx.BoxSizer(wx.HORIZONTAL)

        button = wx.Button(panel, label="Добавить", id=ID_BUT)
        self.button = button
        hbox.Add(self.button, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.BOTTOM, border=10)

        button = wx.Button(panel, label="Прочитать из файла", id=ID_BUTR)
        self.button = button
        hbox.Add(self.button, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.BOTTOM, border=10)

        vbox.Add(hbox, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.BOTTOM)

        panel.SetSizer(vbox)
        self.Bind(wx.EVT_BUTTON, self.add, id=ID_BUT)
        self.Bind(wx.EVT_BUTTON, self.read, id=ID_BUTR)

    def read(self, event):
        name, country, years = None, None, None
        dlg = wx.FileDialog(None, message='Выберите файл',
                            defaultDir='', defaultFile='',
                            wildcard='*.*', style=wx.FLP_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            tree = ET.parse(dlg.GetPath())
            root = tree.getroot()
            for child in root:
                if child.tag == 'name':
                    name = child.text
                if child.tag == 'country':
                    country = child.text
                if child.tag == 'years':
                    life = child.attrib['born'] + '-' + child.attrib['died']
        addAuthor(con, name, country, life)

    def add(self, event):
        name = self.tbt.GetValue()
        country = self.tbs.GetValue()
        life = self.tbi.GetValue()
        addAuthor(con, name, country, life)


app = wx.App()
wnd = MyFrame(None, 'Kravchenko Alina Exercise 2')
wnd.Show(True)
app.MainLoop()


