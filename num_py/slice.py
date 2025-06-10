import numpy as np
import matplot_lib
import scipy


def demo_slice():
    print('------- 二、数组切片和索引 -------')
    print('1、创建切片对象')
    a = np.arange(10)
    s = slice(2, 7, 2)  # 从索引 2 开始到索引 7 停止，间隔为2
    print(a[s])

    print('2、冒号分隔切片参数 start:stop:step')
    print(a[2:7:2])  # 从索引 2 开始到索引 7 停止，间隔为 2

    print('3、多维数组切片')
    a = np.array([[1, 2, 3], [3, 4, 5], [4, 5, 6]])
    print(a)
    # 从某个索引处开始切割
    print('从数组索引 a[1:] 处开始切割，结果为')
    print(a[1:])

    print('4、...省略号切片')
    a = np.array([
        [1, 2, 3],
        [3, 4, 5],
        [4, 5, 6]])
    print(a[..., 1])  # 第2列元素
    print(a[1, ...])  # 第2行元素
    print(a[..., 1:])  # 第2列及剩下的所有元素


