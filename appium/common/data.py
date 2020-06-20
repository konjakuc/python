# -*- coding: utf-8 -*-

command_executor = 'http://127.0.0.1:4723/wd/hub'

desired_caps = {
    'platformName': 'Android',
    'platformVersion': '5.1',
    'deviceName': '123456',
    'appPackage': 'com.example.todolist',
    'appActivity': '.LoginActivity'
}