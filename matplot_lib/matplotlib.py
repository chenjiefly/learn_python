import numpy as np
import matplotlib
from matplotlib import pyplot as plt

# matplotlib教程：https://www.runoob.com/numpy/numpy-matplotlib.html
# 注意该文档底部有更详细的教程1和教程2

# 默认不支持中文字体，可以设置使用mac系统中的中文字体
matplotlib.rcParams['font.family'] = 'STFangsong'  # 使用仿宋字体


def fun_implicit(x, y):
    return x ** 2 * np.sin(x + y ** 2) + y ** 2 * np.exp(x) + 6 * np.cos(x ** 2 + y)


def fun_circle(x, y):
    return x**2 + y**2 - 9  # 圆方程


def draw_fun_implicit():
    x = np.linspace(-6, 6, 100)
    y = np.linspace(-6, 6, 100)
    X, Y = np.meshgrid(x, y)
    Z = fun_implicit(X, Y)
    # Z = fun_circle(X, Y)
    plt.contour(X, Y, Z, levels=[0], colors='blue')  # 画出 fun(x, y) = 0 的等高线轮廓
    plt.title('绘制隐函数x^2*sin(x+y^2)+y^2*exp(x)+6*cos(x^2+y)=0')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
    plt.axvline(0, color='black', linewidth=0.5, linestyle='--')
    plt.grid()
    plt.axis('equal')  # 保持比例
    plt.show()


def demo_matplotlib():
    print('------- 四、矩阵绘图matplotlib -------')
    print('1、绘制折线图')
    x = np.arange(1, 10)
    y = 2 * x + 5
    plt.title("折线图")
    plt.xlabel("年级")
    plt.ylabel("分数")
    plt.plot(x, y, "-.b")
    plt.show()

    print('2、绘制正弦波')
    x = np.arange(0, 2 * np.pi, 0.01)
    y = np.sin(x)
    plt.title("正弦波形图")
    plt.grid(True)  # 开启网格
    plt.plot(x, y)
    plt.show()

    print('3、绘制隐函数')
    draw_fun_implicit()
