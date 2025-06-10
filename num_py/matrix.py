import numpy as np
import matplot_lib
import scipy


# matrix教程：https://www.runoob.com/numpy/numpy-matrix.html

def demo_matrix():
    print('------- 三、矩阵Matrix -------')
    print('1、创建矩阵')
    a = np.matrix('1,2;3,4')
    print(f'a={a}')
    b = np.array([[5, 6], [7, 8]])
    print(f'b={b}')
    c = np.asmatrix(b)  # 由ndarray转换为matrix
    print(f'c={c}')
    d = np.asarray(c)  # 由matrix转换为ndarray
    print(f'd={d}')

    # 同样可以使用np.matrix.zeros, np.matrix.ones, np.matrix.empty来创建

    print(f'生成N×M单位矩阵={np.eye(3, 4, 0, dtype=float)}')
    print(f'生成N阶方阵单位矩阵={np.identity(5, dtype=int)}')
    print(f'随机数矩阵={np.random.rand(3, 4)}')

    print('2、矩阵的转置')
    print(f'方法1、a.T={a.T}')
    print(f'方法2、numpy.transpose(a)={np.transpose(a)}')

    print('3、矩阵乘法的4种方法')
    print(f'a*c={a*c}')  # 只适用matrix
    # 以下3种方法都适用于ndarray和matrix
    print(f'a@c={a@c}')
    print(f'numpy.dot(a, c)={np.dot(a, c)}')
    print(f'numpy.matmul(a, c)={np.matmul(a, c)}')

    print('4、求多项式的根（不精确，推荐使用sympy')
    coefficients = [1, -2, 1]
    # coefficients = [1, 0, -1]
    print(f'x^2-2x+1={np.roots(coefficients)}')

    print('5、求解线性矩阵方程')
    # 2x+3y=5
    # 4x+y=6
    A = np.array([[2, 3],  # 定义系数矩阵A
                  [4, 1]])
    b = np.array([5, 6])  # 定义目标向量b
    solution = np.linalg.solve(A, b)
    print('解二元一次方程组的解为：', solution)
