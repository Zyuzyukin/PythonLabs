import numpy
from numpy.linalg import det, inv


def multimatrix():
    print('Task 1:')
    first_matrix = numpy.arange(3 * 5).reshape((3, 5))
    second_matrix = numpy.arange(5 * 2).reshape((5, 2))

    print('First:\n', first_matrix)
    print('Second:\n', second_matrix)
    print('Mult: \n', first_matrix @ second_matrix)
    print()

def multivector():
    print('Task 2: ', end='')
    matrix = numpy.arange(2 * 3).reshape((3, 2))
    vector = numpy.array([1, -1], dtype=float)
    print(matrix @ vector)
    print()


def linalg():
    print('Task 3: ', end='')
    # 2x + 5y = 1
    # x - 10y = 3
    matrix = numpy.array([[2., 5.], [1., -10.]])
    vector = numpy.array([1., 3.])
    print(numpy.linalg.solve(matrix, vector))
    print()


def determin():
    print('Task 4: ', end='')
    matrix = numpy.arange(5 * 5).reshape((5, 5))
    print(det(matrix))
    print()


def invmatrix():
    print('Task 5:')
    a = numpy.array([[0, 4, 2], [4, 6, 6], [7, 9, 10]])
    a_invented = inv(a)
    print(a_invented)
    print()


def transmatrix():
    print('Task 6: ')
    a = numpy.array([[0, 1, 2], [4, 5, 6]])
    a = a.transpose()
    print(a)
    print()



multimatrix()
multivector()
linalg()
determin()
invmatrix()
transmatrix()