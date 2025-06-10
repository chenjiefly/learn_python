import numpy as np
import matplot_lib
import scipy


def demo_create():
    print('------- 一、数组创建 -------')
    print(f'numpy的版本号是：{np.__version__}\n')

    print('1、创建一维数组')
    print(np.array([1, 2, 3]))

    print('2、创建二维数组')
    print(np.array([[1, 2, 3], [4, 5, 6]]))

    print('3、创建全0、全0、全空数组')
    print(np.zeros(shape=(5, 3)))  # shape代表形状为5行3列
    print(np.ones(shape=(5, 3)))

    print('4、创建空数组（值随机的，未初始化）')
    print(np.empty(shape=(5,3)))

    print('5、创建随机数组')
    print(np.random.rand(3, 4))
    print(np.random.random((3, 4)))
    # 创建一个4行5列的随机整数数组，其中每个元素的值在0到5之间
    print(np.random.randint(0, 5, size=(4, 5)))

    print('6、创建有连续序列的数组')
    # 对[0, 10)左闭右开区间，以步长为2采样
    print(np.arange(0, 10, 2))

    print('7、创建等差数列')
    # 生成等差数列，起始start，结束stop，共num项，公差d=(stop - start)/(num - 1)
    # 相当于是对指定数组进行num等分的抽样：对[0, 10]闭区间平均10(11-1)等分，即抽样11个点，包含了左右端点
    print(np.linspace(0, 10, 11))
    print(np.linspace(1, 1, 5))  # 生成5项公差为0的每项都为1的等差数列

    print('8、创建等比数列')
    # 生成等比数列，num为项数，产项为base^start,末项为base^end，中间每项的幂递增公差为(end - start)/(num - 1)
    print(np.logspace(0, 10, 11, base=2, dtype=int))
    # 其实就是生成等差数列，起始start，结束stop，共num项，公差d=(stop - start)/num
    print(np.logspace(1, 1, 5, dtype=int))


