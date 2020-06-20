# -*- coding: utf-8 -*-

class Student(object):
    __id = 1

    def __init__(self, name):
        self.name = name
        self.id = Student.__id
        Student.__id += 1

    def show(self):
        print(self.name, self.id)


stu1 = Student('张三')
stu2 = Student('李四')

stu1.show()
stu2.show()
