# -*- coding: utf-8 -*-

import requests

# get
respBaidu = requests.get("http://www.baidu.com")
print(respBaidu.text)

# post
loginURL = "http://acv3.learn.it101.live/api/auth/login"
payload = {"loginId":"zhangbinxuan","password":"123456","orgId":7}
# respLogin = requests.post(loginURL, payload)
# print(respLogin.json())

# 带cookies的get
trendsAPI = "http://acv3.learn.it101.live/api/courses/v3/trends"
# respTrends = requests.get(trendsAPI, cookies=respLogin.cookies)
# print(respTrends.json())



def printRsponse(response):
    print("\n\n-------HTTP response BEGIN--------")
    print(response.status_code)
    for k,v in response.json().items():
        print(f"{k}:{v}")
    print()
    print(response.content.decode("utf-8"))
    print("\n\n-------HTTP response END--------")


session = requests.session()
response = session.post(loginURL, payload)
printRsponse(response)

response = session.get(trendsAPI)
printRsponse(response)