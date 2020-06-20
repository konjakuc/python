import os
import time

print(os.path.dirname(os.path.abspath(__file__)))
print(os.getcwd())
print(time.time())  # 时间戳
print(time.localtime(time.time()))
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
