class Libs(object):

    def __init__(self, number, adress):
        self.__adress = adress
        self.__number = number
        self.__books = []

    def __add__(self, book):
        self.__books += [book]
        return self

    def __iadd__(self, book):
        return self.__add__(book)

    def __iter__(self):
        for book in self.__books:
            yield book