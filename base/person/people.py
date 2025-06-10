import math


def log_people(text):
    print('  {t}'.format(t=text))
    print(f'\t我是person包中的person模块的log_base方法')
    print('\t名字{name}，年龄{age:6d}'.format(name='子泷'.zfill(7), age=18))


class People:
    # 定义基本属性
    name = ''
    # 定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0

    # 定义构造方法
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.__init_weight(weight)

    def speak(self):
        print('【人类】%s 说: 我 %d 岁，体重%d斤。' % (self.name, self.age, self.__weight))

    def __init_weight(self, weight):
        self.__weight = weight * 2

    def get_weight(self):
        return self.__weight

    def log(self):
        print('log of People')

