import datetime

from django.db import models


# Create your models here.


class User(models.Model):
    SEX = (
        ('M', '男'),
        ('F', '女'),
    )
    nickName = models.CharField(max_length=32, unique=True)
    phoneNum = models.CharField(max_length=16, unique=True)

    sex = models.CharField(max_length=8, choices=SEX)
    birthYear = models.IntegerField()
    birthMonth = models.IntegerField()
    birthDay = models.IntegerField()
    avatar = models.CharField(max_length=256)
    location = models.CharField(max_length=32)

    @property
    def age(self):
        """
        计算用户年龄
        """
        today = datetime.date.today()
        birthDate = datetime.date(self.birthYear, self.birthMonth, self.birthDay)
        times = today - birthDate
        return times.days // 365



