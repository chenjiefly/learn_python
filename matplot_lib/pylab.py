import numpy as np
import matplotlib
import matplotlib.pylab as plt
# from mpl_toolkits.mplot3d import Axes3D
# import scipy


# pylab教程：https://www.runoob.com/w3cnote/matplotlib-tutorial.html

# 默认不支持中文字体，可以设置使用mac系统中的中文字体
matplotlib.rcParams['font.family'] = 'STFangsong'  # 使用仿宋字体


# 定义 peaks 函数
def peaks(x, y):
    return (3 * (1 - x)**2 * np.exp(-(x**2) - (y + 1)**2) -
            10 * (x / 5 - x**3 - y**5) * np.exp(-x**2 - y**2) -
            1/3 * np.exp(-(x + 1)**2 - y**2))


def demo_pylab():
    print('------- 五、pylab 类Matlab风格 -------')
    print('1、绘制正弦图')
    n = 256
    x = np.linspace(-np.pi, np.pi, n, endpoint=True)
    y = np.sin(2 * x)

    plt.grid()
    plt.plot(x, y + 1, color='blue', alpha=1.00)
    plt.plot(x, y - 1, color='red', alpha=1.00)
    plt.show()

    print('2、绘制Matlab经典3D图')
    # 生成 x 和 y 网格数据
    x = np.linspace(-3, 3, 100)
    y = np.linspace(-3, 3, 100)
    x, y = np.meshgrid(x, y)
    # 计算 z 值
    z = peaks(x, y)

    # 创建 3D 图形
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')  # 在fig上创建一个1行1列的子图，并指定唯一的这第1个子图使用3D模式绘图
    surf = ax.plot_surface(x, y, z, cmap='viridis')  # 使用 'viridis' 颜色图

    # 添加颜色条
    cbar = fig.colorbar(surf, shrink=0.5, aspect=5)
    cbar.set_label('Z轴色值')

    # 添加标题和标签
    ax.set_title('Peaks函数 - 3D绘图')
    ax.set_xlabel('X轴')
    ax.set_ylabel('Y轴')
    ax.set_zlabel('Z轴')

    # 显示图形
    plt.show()

