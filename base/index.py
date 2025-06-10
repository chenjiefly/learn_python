# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import sys
import os
# 包的引用方式
from . import person  # 导出当前base目录下的person包
from .person import *  # 【不推荐】导出当前base目录下的person包中的__init__中指定的所有变量
from .person import people  # 导出当前base目录下people模块
from .person.people import log_people as log_people_fun  # 导出包.模块中的方法
# 模块的引用方式
from .util import print_name as print_input_name, PI  # 可以一次性引用多个变量
from base import util
# 面向对象
from .person.people import People
from .person.student import Student
from .person.speaker import Speaker


def test_package():
    print('\n--------- 测试包 ---------')
    person.people.log_people(f'1.导出包，间接调用包.模块.方法！')
    log_people(f'2.导出包中所有*！')
    people.log_people(f'3.导出包.模块，间接调用模块.方法！')
    log_people_fun(f'3.导出包.模块.方法，直接调用方法！')


def test_module():
    print('\n--------- 测试模块 ---------')
    print_input_name(f'1.直接导出模块方法！ PI={PI}')
    util.print_name(f'2.导出模块再引用方法！PI={util.PI}')
    print(f'模块内所有的变量名：{dir(util)}')


class MyError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


def test_except():
    print('\n------ 触发异常错误 ------')
    try:
        n = int(input('请输入正整数，否则触发异常：'))
        print(f'输入的数字是：{n}')

        if n == 0:
            raise MyError('不能输入0（自定义MyError异常）')
        elif n < 0:
            raise Exception('不能输入负整数（自定义异常）')
    except ValueError as err:
        print(f'\t触发传值异常！({err})')
    except TypeError as err:
        print(f'\t触发类型异常！({err})')
    except MyError as e:
        print('\t数值输入异常:', e.value)
    except:  # 最后一个可以不写错误类型，用作兜底
        print(f'\t触发未知异常！({sys.exc_info()[0]})')
        raise  # 只想知道是否抛出一个异常，而不想处理时，可以再次向外抛出该异常
    else:
        print('\t没有异常发生时才会执行的代码')
    finally:
        print('\t不管有没有异常都会执行的代码')


def test_class():
    print('\n-------- 基类 --------')
    p = People('chenjie', 18, 75)
    p.speak()
    print('\n-------- 单继承 --------')
    s = Student('cj85996', 28, 80, 1)
    s.speak()
    super(Student, s).speak()  # 找到Student的父类，把s转换为父类对象，再执行speak方法

    print('\n-------- 多继承 --------')
    speaker = Speaker('chenjie', 38, 85, 10, 'python入门', '成熟稳健型', '顶级')
    speaker.speak()

    print('\n-------- 类的私有属性 --------')
    print(f'公有属性 name={speaker.name}，私有属性 __weight={speaker.get_weight()}')
    print(f'静态属性level={Speaker.level}，实例属性level={speaker.level}')

    print('\n-------- 【重点】多继承时方法解析顺序MRO（Method Resolution Order） --------')
    print(Speaker.mro())  # Speaker.mro() 或 Speaker.__mro__
    speaker.log()


class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return 'Vector (%d, %d)' % (self.a, self.b)

    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)

    def __sub__(self, other):
        return Vector(self.a - other.a, self.b - other.b)

    def __mul__(self, other):
        return Vector(self.a * other.a, self.b * other.b)

    def __truediv__(self, other):
        return Vector(self.a / other.a, self.b / other.b)

    def __floordiv__(self, other):
        return Vector(self.a // other.a, self.b // other.b)

    def __mod__(self, other):
        return Vector(self.a % other.a, self.b % other.b)

    def __pow__(self, power, modulo=None):
        return Vector(self.a ** power.a, self.b ** power.b)

    def __eq__(self, other):
        return (self.a == other.a) and (self.b == other.b)


def test_override_operator():
    print('\n-------- 运算符重载 --------')
    v1 = Vector(2, 2)
    v2 = Vector(3, 3)
    print(f'v1 = {v1}')
    print(f'v2 = {v2}')
    print(f'v1 + v2 = {v1 + v2}')
    print(f'v1 - v2 = {v1 - v2}')
    print(f'v1 * v2 = {v1 * v2}')
    print(f'v1 / v2 = {v1 / v2}')
    print(f'v1 // v2 = {v1 // v2}')
    print(f'v1 % v2 = {v1 % v2}')
    print(f'v1 ** v2 = {v1 ** v2}')


def test_iteration():
    print('\n------- 迭代器示例：斐波那契数列 -------')

    def fibonacci(n):  # 生成器函数 - 斐波那契
        a, b, counter = 0, 1, 0
        while True:
            if counter > n:
                return
            yield a
            a, b = b, a + b
            counter += 1

    f = fibonacci(10)  # f 是一个迭代器，由生成器返回生成
    while True:
        try:
            print(next(f), end=" ")
        except StopIteration:
            sys.exit()


# Press the green button in the gutter to run the script.
def run():
    test_package()
    test_module()
    test_except()
    test_class()
    test_override_operator()
    test_iteration()

    # 海象运算符：赋值的同时返回该值
    if (a := 1) > 0:
        print(str(a) + '是正数')

