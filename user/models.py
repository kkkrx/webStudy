import datetime

from django.db import models
from django.utils.functional import cached_property

# Create your models here.


class User(models.Model):
    """
    用户数据模型
    """
    SEX = (
        ('M', '男'),
        ('F', '女'),
    )
    nickName = models.CharField(max_length=32, unique=True)
    phoneNum = models.CharField(max_length=16, unique=True)

    sex = models.CharField(max_length=8, choices=SEX)
    birthYear = models.IntegerField(default=2000)
    birthMonth = models.IntegerField(default=1)
    birthDay = models.IntegerField(default=1)
    avatar = models.CharField(max_length=256)
    location = models.CharField(max_length=32)

    @cached_property
    def age(self):
        """
        计算用户年龄
        """
        today = datetime.date.today()
        birthDate = datetime.date(self.birthYear, self.birthMonth, self.birthDay)
        times = today - birthDate
        return times.days // 365

    @property
    def profile(self):
        """
        该用户的配置项
        """
        if not hasattr(self, 'myProfile'):
            self.myProfile, _ = Profile.objects.get_or_create(id=self.id)
        return self.myProfile


class Profile(models.Model):
    """
    用户配置项
    """
    SEX = (
        ('M', '男'),
        ('F', '女'),
    )

    location = models.CharField(max_length=32, verbose_name='目标城市')

    minDistance = models.IntegerField(default=1, verbose_name='最小查找范围')
    maxDistance = models.IntegerField(default=10, verbose_name='最大查找范围')

    minDatingAge = models.IntegerField(default=18, verbose_name='最小交友年龄')
    maxDatingAge = models.IntegerField(default=45, verbose_name='最大交友年龄')

    datingSex = models.CharField(max_length=8, choices=SEX, verbose_name='匹配的性别')

    vibration = models.BooleanField(default=True, verbose_name='是否开启震动')
    onlyMat = models.BooleanField(default=True, verbose_name='不让未匹配的人看我的相册')
    autoPlay = models.BooleanField(default=True, verbose_name='是否自动播放视频')