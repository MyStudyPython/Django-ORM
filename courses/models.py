# 从数据库导入models类
from django.db import models


# Create your models here.
# 类名就是我们的表名
class Test(models.Model):
    """测试学习用"""

    # 自增长字段 ---比如数据的序号
    Auto = models.AutoField()  # 自增长字段 默认是int类型
    BigAuto = models.BigAutoField()  # bigAutoField 表示范围更大

    # 二进制数据
    Binary = models.BinaryField()

    # 布尔型
    Boolean = models.BooleanField()  # 不允许为空的Boolean类型
    NullBoolean = models.NullBooleanField()  # 允许为空的Boolean类型

    # 整型
    PositiveSmallInteger = models.PositiveSmallIntegerField()  # 正整数并且大小为5个字节
    SmallInteger = models.SmallIntegerField()  # 整数（正负皆可）并且为6个字节
    PositiveInteger = models.PositiveIntegerField()  # 正整数并且10个字节
    Integer = models.IntegerField()  # 整数（正负皆可）并且11个字节
    BigInteger = models.BigIntegerField()  # 整数（正负皆可）并且 20个字节

    # 字符串类型
    Char = models.CharField()  # 对应的是varchar,通常会指定一个长度 max_length
    Text = models.TextField()  # 对应的是longtext,不需要指定长度

    # 时间日期类型
    Date = models.DateField()  # 年月日
    DateTime = models.DateTimeField()  # 年月日时分秒
    Duration = models.DurationField()  # 一段时间，是int类型 底层是python的timedelta实现

    # 浮点类型
    Float = models.FloatField()  #
    Decimal = models.DecimalField()  # 需要指定整数有多少位，小数有多少位

    # 其他字段
    Email = models.EmailField()  # 邮箱
    Image = models.ImageField()  # 图片
    File = models.FileField()  # 文件
    FilePath = models.FilePathField()  # 文件地址
    URL = models.URLField()  # 浏览器中输入的url地址
    UUID = models.UUIDField()  # uuid
    GenericIPAddress = models.GenericIPAddressField()  # IP地址 ipv4和ipv6都可以

    class Meta:
        verbose_name = "测试"
        verbose_name_plural = verbose_name

    def __self__(self):
        return self.name


class A(models.Model):
    # 一对一关系 关联模型类Test
    oneToOne = models.OneToOneField(Test)


class B(models.Model):
    # 一对多关系 关联到模型A
    ForeignKey = models.ForeignKey(A)


class C(models.Model):
    # 多对多的关系 关联到模型B
    manyToMany = models.ManyToManyField(B)
