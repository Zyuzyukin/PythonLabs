import wx
import xml.etree.ElementTree as ET
import json
import sqlite3

ID_X = 1
ID_J = 2

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
    s = []
    for value in cursor.execute("SELECT * FROM author"):
        value = str(value[0]) + ' - ' + str(value[1]) + ' - ' + str(value[2]) + ' - ' + str(value[3])
        s.append(value)
    return s
    con.commit()


con = sql_connection()


class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, title=title)
        self.SetSize((500, 400))

        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)

        vbox.Add((wx.StaticText(panel, label="Все авторы:")), flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=50)
        tb = wx.CheckListBox(panel, choices=table(con),
                             style=wx.TE_MULTILINE | wx.TE_READONLY | wx.HSCROLL | wx.TE_RICH)
        self.tb = tb
        vbox.Add(tb, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.BOTTOM, border=15, proportion=1)
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        buttonJ = wx.Button(panel, label="Сохранить в json", id=ID_J)
        self.buttonJ = buttonJ
        buttonX = wx.Button(panel, label="Сохранить в XML", id=ID_X)
        self.buttonX = buttonX
        hbox.Add(self.buttonJ, flag=wx.EXPAND | wx.ALL, border=50)
        hbox.Add(self.buttonX, flag=wx.EXPAND | wx.ALL, border=50)
        vbox.Add(hbox, flag=wx.EXPAND)
        panel.SetSizer(vbox)
        self.Bind(wx.EVT_BUTTON, self.enterJ, id=ID_J)
        self.Bind(wx.EVT_BUTTON, self.enterX, id=ID_X)

    def enterX(self, event):
        check = self.tb.GetCheckedStrings()
        for i in check:
            author_info = i.split(' - ')
            ID, name, country, years = author_info
            xml = '''
        <?xml version="1.0"?>
        <author>
            <name>''' + name + '''</name>
            <country>''' + country + '''</country>
            <years ="''' + years + '''"/>
        </author>
        '''
            with open(str(name) + '.xml', 'w') as f:
                f.write(xml)

    def enterJ(self, event):
        check = self.tb.GetCheckedStrings()
        for i in check:
            author_info = i.split(' - ')
            ID, name, country, years = author_info
            with open(str(name) + '.json', 'w') as f:
                f.write(json.dumps(author_info))


app = wx.App()
wnd = MyFrame(None, 'Kravchenko Alina Exercise 2')
wnd.Show(True)
app.MainLoop()