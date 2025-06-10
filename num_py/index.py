import numpy as np
# import matplot_lib
# import scipy
from .create import demo_create
from .slice import demo_slice
from .matrix import demo_matrix

# 教程：https://www.runoob.com/numpy/numpy-tutorial.html


def run():
    print('------- 数值计算（numerical calculation） -------')
    print(f'numpy的版本号是：{np.__version__}\n')
    demo_create()
    demo_slice()
    demo_matrix()


