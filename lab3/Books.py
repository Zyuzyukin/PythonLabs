

from Taggable import Taggable
class Books(Taggable):
    count = 0

    def __init__(self, author, name):
        if name == '' or author == '':
            raise ValueError('Имя автора не указано!')
        else:
            Books.count += 1
            self.__name = name
            self.__author = author
            self.__code = Books.count

    def tag(self):
        list_tg = []
        words = self.__name.split()
        for i in words:
            if i.istitle():
                list_tg.append(i)
        return list_tg

    def __str__(self):
        return "[%d] %s '%s'" % ( self.__code, self.__author, self.__name)