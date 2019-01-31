from django.db import models
from django.contrib.auth.models import AbstractUser




class UserProfile(AbstractUser):
    """公共用户信息表"""
    sex_Choices= (
        (0,"女"),
        (1,"男"),
    )

    name = models.CharField(max_length=32,verbose_name="中文名")
    age = models.IntegerField(verbose_name="年龄",default=12)
    sex = models.CharField(verbose_name="性别", choices=sex_Choices,max_length=8,default="0")
    hight = models.CharField(verbose_name="身高",max_length=8,default="160")
    addr = models.CharField(verbose_name="家庭住址",max_length=128,default="")
    number = models.CharField(verbose_name="工号/学号",max_length=32,unique=True)


class Classes(models.Model):
    """班级表"""
    name = models.CharField(verbose_name="班级名",max_length=16)
    lever = models.CharField(verbose_name="年级",max_length=8)
    Classroom = models.CharField(verbose_name="教学楼",max_length=16)

class Teacher(models.Model):
    """教师表"""
    dir_Choices = (
        (0,"不是"),
        (1,"是")
    )

    user = models.OneToOneField(UserProfile,on_delete=models.CASCADE,) # models.CASCADE : 主表的数据被删除,关联的数据同样被自动删除
    cls = models.ManyToManyField(Classes) # 一个老师对应多个班级 / 一个班级有多个老师
    Is_director = models.CharField(verbose_name="班主任",choices=dir_Choices,max_length=16,default=0)

class Student(models.Model):
    """学生表"""
    user = models.OneToOneField(UserProfile,on_delete=models.CASCADE,to_field="username")
    tea = models.ManyToManyField(Teacher) # 一个学生对应多个老师 / 一个老师对应多个学生
    cls = models.ForeignKey(Classes,verbose_name="班级",on_delete=models.CASCADE) # 一个学生对应一个班级 / 一个班级对应多个学生
