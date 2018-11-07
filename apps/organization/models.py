from django.db import models
from datetime import datetime


# Create your models here.
# 城市字典
class CityDict(models.Model):
    name = models.CharField(max_length=20, verbose_name=u"city")
    # 城市描述：备用不一定展示出来
    desc = models.CharField(max_length=200, verbose_name=u"city description")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"added time")

    class Meta:
        verbose_name = u"city"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.name

# 课程机构
class CourseOrg(models.Model):
    name = models.CharField(max_length=50, verbose_name=u"org name")
    # 机构描述，后面会替换为富文本展示
    desc = models.TextField(verbose_name=u"org description")
    click_nums = models.IntegerField(default=0, verbose_name=u"click")
    fav_nums = models.IntegerField(default=0, verbose_name=u"favourite number")
    image = models.ImageField(
        upload_to="org/%Y/%m",
        verbose_name=u"figure",
        max_length=100)
    address = models.CharField(max_length=150, verbose_name=u"org address")
    # 一个城市可以有很多课程机构，通过将city设置外键，变成课程机构的一个字段
    # 可以让我们通过机构找到城市
    city = models.ForeignKey(CityDict, verbose_name=u"city",on_delete=models.CASCADE)
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"added time")

    class Meta:
        verbose_name = u"course org"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.name


# 讲师
class Teacher(models.Model):
    # 一个机构会有很多老师，所以我们在讲师表添加外键并把课程机构名称保存下来
    # 可以使我们通过讲师找到对应的机构
    org = models.ForeignKey(CourseOrg, verbose_name=u"org",on_delete=models.CASCADE)
    name = models.CharField(max_length=50, verbose_name=u"teacher name")
    work_years = models.IntegerField(default=0, verbose_name=u"work years")
    work_company = models.CharField(max_length=50, verbose_name=u"work company")
    work_position = models.CharField(max_length=50, verbose_name=u"work position")
    points = models.CharField(max_length=50, verbose_name=u"points")
    click_nums = models.IntegerField(default=0, verbose_name=u"click")
    fav_nums = models.IntegerField(default=0, verbose_name=u"favourite number")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"added time")

    class Meta:
        verbose_name = u"teacher"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "[{0}]'s teacher: {1}".format(self.org, self.name)