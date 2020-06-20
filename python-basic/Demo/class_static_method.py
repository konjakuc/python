# !/usr/bin/env python
# -*- coding: utf-8 -*-

class Student(object):

    def intro(self):  # 只能实例调用
        print(self)
        print("实例方法")

    @classmethod
    def introClass(cls):  # 通常是类调用
        print(cls)
        print(cls == Student)  # True
        print("类方法")

    @staticmethod
    def introStatic():  # 类和实例都可调用
        print("静态方法")

    def test(self):
        self.intro()
        self.introClass()
        self.introStatic()
        Student.intro(self)  # 本质上 == self.intro()
        Student.introClass()
        Student.introStatic()

stu = Student()
stu.test()