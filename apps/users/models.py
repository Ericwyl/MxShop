from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractUser

# Create your models here.


class UserProfile(AbstractUser):
    '''
    用户信息
    '''
    GENDER_CHOICES = (
        ("male", u"男"),
        ("female", r"女")
    )
    #用户用手机注册，所以姓名、生日、邮箱可以为空
    name = models.CharField("姓名", max_length=30, null=True, blank=True)
    birthday = models.DateField("出生年月", null=True, blank=True)
    gender = models.CharField("性别", max_length=6, choices=GENDER_CHOICES, default="female")
    mobile = models.CharField("电话", max_length=11)
    #null = True,表示该字段可为空，blank=True表示表单填写该字段时可为空
    email = models.EmailField("邮箱", max_length=100, null=True, blank=True)

    class Meta:
        # db_table = "tab_userprofile" #一般情况下我们这边会再定义一个表名，，如果不定义的话，默认为app名_类名,users_userprofile
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class verifyCode(models.Model):
    '''
    验证码
    '''
    code = models.CharField("验证码", max_length=10)
    mobile = models.CharField("手机号", max_length=11)
    add_time = models.DateTimeField("添加时间", default=datetime.now)

    class Meta:
        # db_table = "tab_verifyVode"
        verbose_name = "短信验证"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.code












