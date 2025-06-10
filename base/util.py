import math

PI = math.pi


def print_name(name):
    print(f'打印的名字是：{name}')
    return


if __name__ == '__main__':  # 用该判断来区分当前脚本是否被执行
    print(f'程序自身在运行，模块名：{__name__}')
else:
    print(f'我来自另一模块，模块名：{__name__}')  # 当前脚本没有被执行，只是被其他脚本引用才执行

