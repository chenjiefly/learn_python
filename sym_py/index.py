import numpy as np
from sympy import (Symbol, symbols, sin, cos, exp,
                   Eq, solve,
                   simplify, trigsimp,
                   collect, expand, factor,
                   diff, integrate)


def run():
    print('------- 符号代数运算（sympy） -------')
    x = Symbol('x')
    y = x**2
    print(f'当x=3时，y=x^2的值为{y.subs(x, 3)}')

    x, y = symbols('x y')
    equation = Eq(x**2 + 2 * x - 3, 0)  # 设置方程 x^2 + 2x - 3 = 0
    solution = solve(equation, x)
    print(f'解一元二次方程x^2 + 2x - 3 = 0的结果为x={solution}')  # 输出: Solution: [2]

    equation1 = x + y - 3  # 第一个方程
    equation2 = 2*x + y - 4  # 第二个方程
    solutions = solve((equation1, equation2), (x, y))
    print(f'解二元一次方程组：x+y-3=0和2x+y-4=0的结果为={solutions}')  # 输出: Solution: [2]

    print(f'化简表达式(x^2 - 1)(x-1)的结果为：{simplify((x**2 - 1) / (x - 1))}')

    print(f'化简三角函数2sin(x)cos(x)的结果为：{trigsimp(2*sin(x)*cos(x))}')

    print(f'按x合并多项式(x^3+2x^2*y+x^2*y^2-y^3)的结果为：{collect(x**3 + 2*x**2*y + x**2*y**2 - y**3, x)}')

    print(f'展开多项式(x + 1) * (x - 2)的结果为：{expand((x + 1) * (x - 2))}')

    print(f'因式分解x**2-x-2的结果为：{factor(x**2-x-2)}')

    print(f'求微分e^(x^2)的结果为：{diff(exp(x**2),x)}')

    print(f'求1/(1+x**2)的不定积分的结果为：{integrate(1/(1+x**2))}')


