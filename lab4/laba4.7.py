from sympy import *


def graph():
    x = Symbol('x')
    func = sin(x)
    print('Функция: ', str(func))
    print('Производная: ', end='')
    differencial = diff(func)
    pprint(differencial)
    plot(differencial)

    print('\nИнтеграл: ')
    integral = integrate(func)
    pprint(integral)
    print('\n')
    plot(integral)


def solution(*equalities):
    if len(equalities) == 1:
        return solve(equalities[0])
    return solve_poly_system(equalities)


def ur():
    x, y = symbols('x y')
    eq1 = Equality(3, x**2 - y)
    eq2 = Equality(9, x*(y **3) )
    eq3 = Equality(2/x, -8)
    pprint(solution(eq1, eq2))
    pprint(solution(eq3))



graph()
print('\n')
ur()