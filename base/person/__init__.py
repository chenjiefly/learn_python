from .people import log_people
from .people import People
from .student import Student

# 如果包定义文件 __init__.py 存在一个叫做 __all__ 的列表变量
# 那么在使用 from package import * 的时候就把这个列表中的所有名字作为包内容导入
__all__ = ['log_people', 'People', 'Student']
