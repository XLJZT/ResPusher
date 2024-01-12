import requests
from ResPusher.respusher import ResPusher
BASEURL = 'http://wxpusher.zjiecode.com/api'

class WxPusher(ResPusher):
    """
    WxPusher Python SDK.
    appToken: str
    uids: list
    """
    def __init__(self, apptoken="", uids=[]):
        """
        初始化 WxPusher 配置, \n
        apptoken 为必填项, \n
        uids 为推送用户的 uid 列表, 默认为空列表.
        """
        self.apptoken = apptoken
        self.uids = uids

    '''
    content: str 
    '''
    def send_message(self, title='', content=""):
        """
        Send Message.\n
        content为发送的内容, 默认为空字符串.
        """
        payload = {
            'appToken': self.apptoken,
            'summary':title,
            'content': content,
            'contentType': 1,
            'uids': self.uids,
            'url': 'https://wxpusher.zjiecode.com',
        }
        url = f'{BASEURL}/send/message'
        res = requests.post(url, json=payload).json()

        if(res.get('code') == 1000):
            print('发送成功')
            return 'success'
        else:
            print('发送失败')
            return 'failed'