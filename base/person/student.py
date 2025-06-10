import random
from .people import People


class Student(People):
    grade = None

    def __init__(self, name, age, weight, grade):
        # 调用父类的构函
        People.__init__(self, name, age, weight)
        self.grade = grade

    # 覆写父类的方法
    def speak(self):
        super().speak()  # 调用父类方法
        print('\t【学生】%s 说: 我 %d 岁了，我在读 %d 年级' % (self.name, self.age, self.grade))

    def log(self):
        print('log of Student')
        super().log()

