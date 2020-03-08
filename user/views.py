from user.logic import sendVerifyCode


# Create your views here.

def getVerifyCode(request):
    """
    手机注册
    """
    phoneNum = request.Get.get('phoneNum')
    response = sendVerifyCode(phoneNum)

    pass


def login(request):
    """
    短信验证码登录
    """
    pass


def getProfile(request):
    """
    获取个人资料
    """
    pass


def modifyProfile(request):
    """
    修改个人资料
    """
    pass


def headSculpture(request):
    """
    头像上传
    """
    pass
