import time


# 匿名函数
func = lambda a, b: a * b
print(func(10, 2))


# 闭包
def outer():
    def inner():
        print("我是里面的函数")
    return inner
outer()()


# 递归求阶乘
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)
print(factorial(10))


# 装饰器
def deco(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print("这个函数执行了", end - start, "秒")
    return wrapper
@deco
def func():
    print("Hello")
    time.sleep(1)
    print("World")
func()