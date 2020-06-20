# -*- coding: utf-8 -*-

import threading

class MyThread(threading.Thread):
    def __init__(self,name=None):
        super().__init__(name=name)

    def run(self):
        for i in range(1,101):
            print(threading.current_thread().getName(),'：',i)
t1 =MyThread("张三")
t1.start()

t2 =MyThread("李四")
t2.start()

t3 =MyThread("王五")
t3.start()


# # 方式一
# def action():
#     for i in range(1, 11):
#         print(threading.current_thread().getName(), '：', i)
#
#
# t1 = threading.Thread(target=action, name="线程1")
# t1.start()
#
#
# # 方式二
# class MyThread(threading.Thread):
#
#     def __init__(self, name: str = None):
#         super().__init__(name=name)
#
#     def run(self):
#         for i in range(1, 11):
#             print(threading.current_thread().getName(), '：', i)
#
# t2 = MyThread()
# t2.setName('线程2')
# t2.start()
#
