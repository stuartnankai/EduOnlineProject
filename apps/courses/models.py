from django.db import models

# Create your models here.
from datetime import datetime

# course info
class Course(models.Model):
    DEGREE_CHOICES = (
        ("cj", u"Junior"),
        ("zj", u"Middle"),
        ("gj", u"Senior")
    )
    name = models.CharField(max_length=50, verbose_name=u"course name")
    desc = models.CharField(max_length=300, verbose_name=u"course description")
    # TextField允许我们不输入长度。可以输入到无限大。暂时定义为TextFiled，之后更新为富文本
    detail = models.TextField(verbose_name=u"course detail")
    degree = models.CharField(choices=DEGREE_CHOICES, max_length=2)
    # 使用分钟做后台记录(存储最小单位)前台转换
    learn_times = models.IntegerField(default=0, verbose_name=u"learning time(mins)")
    # 保存学习人数:点击开始学习才算
    students = models.IntegerField(default=0, verbose_name=u"learning number")
    fav_nums = models.IntegerField(default=0, verbose_name=u"favourite number")
    image = models.ImageField(
        upload_to="courses/%Y/%m",
        verbose_name=u"figure",
        max_length=100)
    # 保存点击量，点进页面就算
    click_nums = models.IntegerField(default=0, verbose_name=u"click")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"added time")

    class Meta:
        verbose_name = u"course name"
        verbose_name_plural = verbose_name

# chapter
class Lesson(models.Model):
    # 因为一个课程对应很多章节。所以在章节表中将课程设置为外键。
    # 作为一个字段来让我们可以知道这个章节对应那个课程
    course = models.ForeignKey(Course, verbose_name=u"course name",on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name=u"chapter name")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"added time")

    class Meta:
        verbose_name = u"chapter name"
        verbose_name_plural = verbose_name


# video for chapter
class Video(models.Model):
    # 因为一个章节对应很多视频。所以在视频表中将章节设置为外键。
    # 作为一个字段来存储让我们可以知道这个视频对应哪个章节.
    lesson = models.ForeignKey(Lesson, verbose_name=u"chapter name",on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name=u"video name")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"added time")

    class Meta:
        verbose_name = u"video name"
        verbose_name_plural = verbose_name


# video resource
class CourseResource(models.Model):
    # 因为一个课程对应很多资源。所以在课程资源表中将课程设置为外键。
    # 作为一个字段来让我们可以知道这个资源对应那个课程
    course = models.ForeignKey(Course, verbose_name=u"course name",on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name=u"name")
    # 这里定义成文件类型的field，后台管理系统中会直接有上传的按钮。
    # FileField也是一个字符串类型，要指定最大长度。
    download = models.FileField(
        upload_to="course/resource/%Y/%m",
        verbose_name=u"source name",
        max_length=100)
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"added time")

    class Meta:
        verbose_name = u"source name"
        verbose_name_plural = verbose_name
