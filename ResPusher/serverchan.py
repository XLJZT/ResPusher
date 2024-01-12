
import urllib.parse
import urllib.request
import json
from ResPusher.respusher import ResPusher

class ServerChan(ResPusher):
    '''
    key: str
    '''
    def __init__(self, key=""):
        '''
        初始化 ServerChan 配置, key 为必填项.
        '''
        self.key = key

    def send_message(self, title='', content=''):
        """
        Send Message.\n
        content为发送的内容, 默认为空字符串.
        """
        postdata = urllib.parse.urlencode({'text': title, 'desp': content}).encode('utf-8')
        url = f'https://sctapi.ftqq.com/{self.key}.send'
        req = urllib.request.Request(url, data=postdata, method='POST')
        with urllib.request.urlopen(req) as response:
            result = response.read().decode('utf-8')
            result = json.loads(result)
        if result.get('code') == 0:
            print("发送成功")
            return "success"
        else:
            print("发送失败")
            return "failed"


