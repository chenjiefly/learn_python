from .student import Student
from .topic import Topic


class Speaker(Student, Topic):
    __level = '初级保密'
    level = '初级'  # 类的静态属性，如果没有同名实例属性，则取静态同名属性的值

    def __init__(self, name, age, weight, grade, title, style, level):
        Student.__init__(self, name, age, weight, grade)
        Topic.__init__(self, title)
        self.style = style
        self.level = level

    def speak(self):
        super(Student, self).speak()
        super().speak()  # Student类
        Student.speak(self)
        Topic.speak(self)

    def log(self):
        print('log of Speaker')
        super().log()  # MRO中Student上就有，所以只执行Student上的
        # super().log1()  # MRO中只有Topic中有，所以只执行Topic上的
