import requests
import json


class ZDUser:
    def __init__(self, username, password):
        self._req = requests.Session()
        self._login(username, password)
        self.username = username

    def _login(self, username, password):
        # login to onlineservice
        self._req.get(
            'https://passport.zhihuishu.com/login?service=https://onlineservice.zhihuishu.com/login/gologin')

        # login
        payload = {
            'code': username,
            'password': password,
            'schoolId': '506'
        }
        r = self._req.post(
            'https://passport.zhihuishu.com/user/validateCodeAndPassword', data=payload)
        res = r.json()
        if res['status'] != 1:
            print(res)
            raise Exception()

        pwd = res['pwd']

        # login to creditqa-web
        self._req.get('https://passport.zhihuishu.com/login', params={
            'pwd': pwd,
            'service': 'https://passport.zhihuishu.com/login?service=https://creditqa-web.zhihuishu.com/'
        })

        # login again
        self._req.get('https://onlineservice.zhihuishu.com/login/gologin')

        # get user info
        r = self._req.get(
            'https://onlineservice.zhihuishu.com/login/getLoginUserInfo')

        self.realName = r.json()['result']['realName']

    def saveQuesion(self, courseId, recruitId, content):
        payload = {
            'recruitId': recruitId,
            'courseId': courseId,
            'content': content,
            'annexs': '[]',
            'sourceType': '2'
        }

        r = self._req.post(
            'https://creditqa-web.zhihuishu.com/shareCourse/saveQuestion', json=payload)
        return r.json()['result']['questionId']

    def saveAnswer(self, quesionId, content):
        payload = {
            'qid': quesionId,
            'aContent': content,
            'source': '2',
            'annexs': '[]'
        }
        r = self._req.post(
            'https://creditqa-web.zhihuishu.com/answer/saveAnswer', data=payload)

        return r.json()['result']['answerId']

    def updateOperationToLike(self, answerId):
        payload = {
            'answerId': answerId,
            'islike': '0',
            'sourceType': '2'
        }
        r = self._req.post(
            'https://creditqa-web.zhihuishu.com/answer/updateOperationToLike', data=payload)
        return r.json()['success']
