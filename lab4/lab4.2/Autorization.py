import wx
import sqlite3
import hashlib

# import Main

ID_BUT_R = 1
ID_BUT_A = 2

DBname = r'library.db'
db = sqlite3.connect(DBname)


def sql_connection():
    try:

        con = sqlite3.connect('library.db')

        return con

    except Error:

        print(Error)


def check_table(con, log, pas):
    cursor = con.cursor()
    for value in cursor.execute("SELECT * FROM password"):
        if value[1] == log and value[2] == pas:
            return True
    return False
    con.commit()


def add_table(con, log, pas):
    cursor = con.cursor()
    i = 0
    for value in cursor.execute("SELECT * FROM password"):
        i = +1
    if i == 0:
        cursor.execute("INSERT INTO password (id_user , login , password ) VALUES (?,?, ?);", (1, log, pas))
    else:
        # id=cursor.execute("SELECT COUNT(*) FROM password")
        print(i)
        cursor.execute("INSERT INTO password (id_user , login , password ) VALUES (?,?, ?);", (i + 1, log, pas))
    con.commit()


con = sql_connection()


class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, title=title)
        self.SetSize((400, 350))

        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)

        vbox.Add((wx.StaticText(panel, label="Авторизация")), flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=25)
        vbox.Add((wx.StaticText(panel, label="")), flag=wx.LEFT | wx.RIGHT | wx.TOP, border=15)
        vbox.Add((wx.StaticText(panel, label="Логин:")), flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=25)
        login = wx.TextCtrl(panel)
        self.login = login
        vbox.Add(self.login, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP | wx.BOTTOM, border=20)

        vbox.Add((wx.StaticText(panel, label="Пароль:")), flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=25)

        password = wx.TextCtrl(panel)
        self.password = password
        vbox.Add(self.password, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP | wx.BOTTOM, border=20)

        hbox = wx.BoxSizer(wx.HORIZONTAL)
        buttonR = wx.Button(panel, id=ID_BUT_R, label="Регистрация")
        self.buttonR = buttonR
        hbox.Add(buttonR, flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=50)
        buttonA = wx.Button(panel, id=ID_BUT_A, label="Авторизация")
        self.buttonA = buttonA
        hbox.Add(buttonA, flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=50)
        vbox.Add(hbox, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP | wx.BOTTOM)
        panel.SetSizer(vbox)

        self.Bind(wx.EVT_BUTTON, self.enterR, id=ID_BUT_R)
        self.Bind(wx.EVT_BUTTON, self.enterA, id=ID_BUT_A)

    def enterR(self, event):
        log = self.login.GetValue()
        pas = self.password.GetValue()
        h = hashlib.md5(pas.encode())
        pas = h.digest()
        add_table(con, log, pas)

    def enterA(self, event):
        log = self.login.GetValue()
        pas = self.password.GetValue()
        pas = self.password.GetValue()
        h = hashlib.md5(pas.encode())
        pas = h.digest()
        rez = check_table(con, log, pas)
        if rez == False:
            dlg = wx.MessageBox('Не верный пароль или логин', '', wx.OK, self)
        else:

            # Main.window()
            # wnd.Close
            print(0)


app = wx.App()
wnd = MyFrame(None, 'Kravchenko Alina Exercise 2')
wnd.Show(True)
app.MainLoop()