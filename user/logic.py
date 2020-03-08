import random

import requests

from webStudy import config
from worker import callByWorker


def genVerifyCode(length=6):
    return random.randrange(10 ** (length - 1), 10 ** length)


@callByWorker
def sendVerifyCode(phoneNum):
    randomCode = genVerifyCode()
    smsCfg = config.HY_SMS_Form.copy()
    smsCfg['content'] = smsCfg['content'] % randomCode
    smsCfg['mobile'] = phoneNum
    response = requests.post(config.HY_SMS_URL, data=smsCfg)
    return response.json()


if __name__ == '__main__':
    message = sendVerifyCode(13718796866)
    print(message)
