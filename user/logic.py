import random

import requests

from webStudy import config


def genVerifyCode(length=6):
    return random.randrange(10 ** (length - 1), 10 ** length)


def sendVerifyCode(phoneNum):
    randomCode = genVerifyCode()
    smsCfg = config.HY_SMS_Form.copy()
    smsCfg['content'] = smsCfg['content'] % randomCode
    smsCfg['mobile'] = phoneNum
    response = requests.post(config.HY_SMS_URL, data=smsCfg)
    return response.json()


message = sendVerifyCode(13718796866)
print(message)