"""
第三方配置
"""


HY_SMS_URL = "http://api.yx.ihuyi.com/webservice/sms.php?method=Submit"

HY_SMS_Form = {
    'account': 'M38041093',
    'password': 'a11e8148bfab233bf00378aeca4f3397',
    'content': '您的验证码是：%s. 请不要把验证码泄露给其他人。',
    'mobile': None,
    'format': 'json'
}