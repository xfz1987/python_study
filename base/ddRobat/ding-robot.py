#!/bin/python
# --*-- coding:utf-8 --*--

'''
钉钉自定义机器人

官方文档: https://open-doc.dingtalk.com/docs/doc.htm?spm=a219a.7629140.0.0.zHt67V&treeId=257&articleId=105735&docType=1
'''

import urllib
import urllib.request
import json
import ssl

# class
class DtalkRobot(object):
    webbhook = ''
    """docstring for ClassName"""
    def __init__(self, webbhook):
        super(DtalkRobot, self).__init__()
        self.webbhook = webbhook

     # 发送Text类型
    def sendText(self, msg, isAll=False, atMobiles=[]):
        data = {
            "msgtype": "text",
            "text": {
                "content": msg
            },
            "at": {
                "atMobiles": atMobiles,
                "isAtAll": isAll
            }
        }
        return self.post(data)

    # 发送markdown类型
    def sendMark(self, title, text, isAll=False, atMobiles=[]):
        data = {
            "msgtype": "markdown",
            "markdown": {
                "title":title,
                "text": text
            },
            "at": {
                "atMobiles": atMobiles,
                "isAtAll": isAll
            }
        }
        return self.post(data)

    # POST操作
    def post(self, data):
        print('=========================')
        # 转换成JSON
        post_data = json.JSONEncoder().encode(data)
        print(post_data)
        # # 设置https
        ssl._create_default_https_context = ssl._create_unverified_context
        req = urllib.request.Request(self.webbhook, str.encode(post_data)) # encode utf8
        req.add_header('Content-Type', 'application/json')
        content = urllib.request.urlopen(req).read()
        # return content

wh = 'https://oapi.dingtalk.com/robot/send?access_token=98f079738adb108a3ce144f199582d89a490ffe9fc90ac64e8d0d6e3ccbcad11'

if __name__ == '__main__':
    dr = DtalkRobot(wh)
    # dr.sendText('测试一下,我是智障', False, ['13810001545'])
    dr.sendMark('测试一下','#今天天气不错\n## 有3-4级风')