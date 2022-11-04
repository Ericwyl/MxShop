import requests
import json


class YunPian(object):
    def __init__(self, api_key):
        self.api_key = api_key
        self.single_send_url = "https://sms.yunpian.com/v2/sms/single_send.json"

    def send_sms(self, code, mobile):
        #需要传递的参数
        params = {
            "apikey": self.api_key,
            "mobile": mobile,
            "text": "【我勒个去】您的验证码是{code}。如非本人操作，请忽略本短信".format(code=code)
        }

        response = requests.post(self.single_send_url, data=params)
        re_dict = json.loads(response.text)
        return re_dict


if __name__ == "__main__":
    #下方填写apikey
    yun_pian = YunPian("dcde8d1a2d5082e35a177a3c7e32ef88")
    yun_pian.send_sms("2022", "17611705725")


