from .matplotlib import demo_matplotlib
from .pylab import demo_pylab

# 教程：https://www.runoob.com/numpy/numpy-tutorial.html


def run(mode=None):
    print('------- 绘图（matplot_lib） -------')
    if mode == '2d':
        demo_matplotlib()
    elif mode == '3d':
        demo_pylab()
    else:
        demo_matplotlib()
        demo_pylab()


