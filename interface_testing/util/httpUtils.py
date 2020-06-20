# -*- coding: utf-8 -*-

import requests
from common.logger import getLogger


class httpUtils:
    logger = getLogger('test')

    def get(self, url, params: dict = None, headers: dict = None):
        res = requests.get(url, data=params, headers=headers)
        self.logger.info("请求路径：" + res.request.url)
        headerStr = ""
        for headerKey in res.request.headers:
            headerStr = headerStr + "\n" + headerKey + ":" + res.request.headers[headerKey]
        self.logger.info("请求头信息：" + headerStr)
        self.logger.info("请求参数：\n" + res.request.body)

        resHeaderStr = ""
        for resHeaderKey in res.headers:
            resHeaderStr = resHeaderStr + "\n" + resHeaderKey + ":" + res.headers[resHeaderKey]
        self.logger.info("响应头信息：" + resHeaderStr)
        self.logger.info("返回结果：\n" + res.content.decode("utf-8"))
        return res

    def post(self, url, params: dict = None, headers: dict = None):
        res = requests.post(url, data=params, headers=headers)
        self.logger.info("请求路径：" + res.request.url)
        headerStr = ""
        for headerKey in res.request.headers:
            headerStr = headerStr + "\n" + headerKey + ":" + res.request.headers[headerKey]
        self.logger.info("请求头信息：" + headerStr)
        self.logger.info("请求参数：\n" + res.request.body)

        resHeaderStr = ""
        for resHeaderKey in res.headers:
            resHeaderStr = resHeaderStr + "\n" + resHeaderKey + ":" + res.headers[resHeaderKey]
        self.logger.info("响应头信息：" + resHeaderStr)
        self.logger.info("返回结果：\n" + res.content.decode("utf-8"))
        return res
