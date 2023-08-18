# 从数据库导入models类
from django.db import models


# Create your models here.
# 类名就是我们的表名
# class Test(models.Model):  # course_test
#     """测试学习用"""

#     # 自增长字段 ---比如数据的序号
#     Auto = models.AutoField()  # 自增长字段 默认是int类型
#     BigAuto = models.BigAutoField()  # bigAutoField 表示范围更大

#     # 二进制数据
#     Binary = models.BinaryField()

#     # 布尔型
#     Boolean = models.BooleanField()  # 不允许为空的Boolean类型
#     NullBoolean = models.NullBooleanField()  # 允许为空的Boolean类型

#     # 整型
#     PositiveSmallInteger = models.PositiveSmallIntegerField(
#         db_column="age"
#     )  # 正整数并且大小为5个字节
#     SmallInteger = models.SmallIntegerField(primary_key=True)  # 整数（正负皆可）并且为6个字节
#     PositiveInteger = models.PositiveIntegerField()  # 正整数并且10个字节
#     Integer = models.IntegerField(verbose_name="11个字节大小")  # 整数（正负皆可）并且11个字节
#     BigInteger = models.BigIntegerField(unique=True)  # 整数（正负皆可）并且 20个字节

#     # 字符串类型
#     Char = models.CharField(
#         max_length=100, null=True, blank=True, db_index=True
#     )  # 对应的是varchar,通常会指定一个长度 max_length
#     Text = models.TextField(help_text="这个是longtext")  # 对应的是longtext,不需要指定长度

#     # 时间日期类型
#     Date = models.DateField(
#         unique_for_date=True,
#         auto_now=True,
#     )  # 年月日
#     DateTime = models.DateTimeField(
#         editable=False, unique_for_month=True, auto_now_add=True
#     )  # 年月日时分秒
#     Duration = models.DurationField()  # 一段时间，是int类型 底层是python的timedelta实现

#     # 浮点类型
#     Float = models.FloatField()  #
#     Decimal = models.DecimalField(max_digits=4, decimal_places=2)  # 需要指定一共有多少位，小数有多少位

#     # 其他字段
#     Email = models.EmailField()  # 邮箱
#     Image = models.ImageField()  # 图片
#     File = models.FileField()  # 文件
#     FilePath = models.FilePathField()  # 文件地址
#     URL = models.URLField()  # 浏览器中输入的url地址
#     UUID = models.UUIDField()  # uuid
#     GenericIPAddress = models.GenericIPAddressField()  # IP地址 ipv4和ipv6都可以

#     class Meta:
#         verbose_name = "测试"
#         verbose_name_plural = verbose_name

#     def __self__(self):
#         return self.name


# class A(models.Model):
#     # 一对一关系 关联模型类Test
#     oneToOne = models.OneToOneField(Test, related_name="one")


# class B(models.Model):
#     # 一对多关系 关联到模型A
#     ForeignKey = models.ForeignKey(A, on_delete=models.CASCADE)  # 删除级联
#     ForeignKey = models.ForeignKey(
#         A, on_delete=models.PROTECT
#     )  # 表示被关联的数据删除时，会报`ProtectedError异常`
#     ForeignKey = models.ForeignKey(
#         A, on_delete=models.SET_NULL, null=True, blank=True
#     )  # 删除置空
#     ForeignKey = models.ForeignKey(A, on_delete=models.SET_DEFAULT, default=0)

#     ForeignKey = models.ForeignKey(A, on_delete=models.DO_NOTHING)

#     ForeignKey = models.ForeignKey(A, on_delete=models.SET())


# class C(models.Model):
#     # 多对多的关系 关联到模型B
#     manyToMany = models.ManyToManyField(B)


class AddressInfo(models.Model):  # couser_addressInfo
    """
    存储省市县地址信息
    """

    address = models.CharField(max_length=200, null=True, blank=True, verbose_name="地址")
    # 自关联数据表需要设置一个自关联字段
    # pid = models.ForeignKey("self", null=True, blank=True, verbose_name="自关联")
    pid = models.ForeignKey(
        "self", null=True, blank=True, verbose_name="自关联", on_delete=models.CASCADE
    )
    # pid = models.ForeignKey("AddressInfo", null=True, verbose_name="自关联")  # 两种写法

    # 这是为了测试下面的联合唯一字段 unique_together 所加的字段
    note = models.CharField(max_length=200, null=True, blank=True, verbose_name="说明")

    """
    这里虽然写的pid
    但是在数据库上显示的 pid_id
    因为在给 ForeignKey字段命名的时候，django会自动将字段名称加上"_id"后缀
    """

    def __str__(self):  # python 2 中写法是 __unicode__ (self)_
        return self.address  # 这里返回地址信息，通常可以返回上面写好的字段

    class Meta:
        # 定义元数据
        db_table = "address"  # 更改数据表，把couser_addressInfo 更改为 address

        ordering = ["pid"]  # 指定按照什么字段进行排序

        verbose_name = "省市县地址信息"  # 模型类设置可读信息
        verbose_name_plural = verbose_name  # 因为英文所有有复数

        # 继承
        # abstact = True  # 设置成基类，让他不生成数据表，直供其他子类来继承

        # permission = (("定义好的权限"), ("给权限的说明"))

        # managed = False  # 是否按照django祭奠的规则来管理模型类，或者是否创建，是否删除数据表

        """
        联合唯一键,对应的mysql里面的联合唯一约束
        可以是一元元组，也可以是二元元组

        一元元组表示只使用一组字段作为约束条件
        多元元组表示每一个元组通过不同的字段进行联合约束
        """
        unique_together = ("address", "note")  # 一元元组
        # unique_together = ((), ())  # 多元元组

        # app_label = 'courses' # 这个等于 setting.py 里面 INATALLS_APP

        # db_tablespace  #定义数据库表空间的名字


class Teacher(models.Model):
    """
    讲师信息表
    """

    name = models.CharField(
        max_length=30, primary_key=True, db_index=True, verbose_name="昵称"
    )
    introduction = models.TextField(default="这位同学很懒，木有签名的说~", verbose_name="简介")
    fans = models.PositiveBigIntegerField(default="0", verbose_name="粉丝数")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    class Meta:
        verbose_name = "讲师信息表"  # 模型类设置可读信息
        verbose_name_plural = verbose_name  # 因为英文所有有复数

    # 给模型对象返回了讲师的昵称
    def __str__(self):  # Python2:__unicode__
        return super().nickname


class Course(models.Model):
    """
    课程信息表
    """

    title = models.CharField(
        max_length=100, primary_key=True, db_index=True, verbose_name="课程名"
    )
    """
    choices 对应数据库的枚举类型

    一般情况下，对于一些可选且有限的字段，可以使用枚举类型

    一来可以t提高查询效率，二来也可以节省空间
    """
    type = models.CharField(
        choices=((1, "实战课"), (2, "免费课"), (0, "其他")),
        max_length=1,
        default=0,
        verbose_name="课程类型",
    )
    price = models.PositiveSmallIntegerField(verbose_name="价格")
    volume = models.BigIntegerField(verbose_name="销量")
    online = models.DateField(verbose_name="上线时间")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    class Meta:
        verbose_name = "课程信息表"
        verbose_name_plural = verbose_name

    def __str__(self):
        """
        get_type_display() 表示获取type选择的值的显示

        get_ + 字段名 + display()
        """
        # return f"{self.get_type_display()}-{self.title}"  # 实例：实战课Django 零基础入门到实战
        return "{}-{}".format(self.get_type_display(), self.title)  # 另一种写法


class Student(models.Model):
    """
    学生信息表
    """

    nickname = models.CharField(
        max_length=30, primary_key=True, db_index=True, verbose_name="昵称"
    )
    age = models.PositiveSmallIntegerField(verbose_name="年龄")
    gender = models.CharField(
        choices=((1, "男"), (2, "女"), (0, "保密")),
        max_length=1,
        default=0,
        verbose_name="性别",
    )
    study_time = models.PositiveIntegerField(default="0", verbose_name="学习时长(h)")
    created_at = models.DateField(auto_now_add=True, verbose_name="创建时间")
    update_at = models.DateField(auto_now=True, verbose_name="更新时间")

    class Meta:
        verbose_name = "学生信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.nickname


class TeacherAssistant(models.Model):
    """
    助教信息表
    """

    nickname = models.CharField(
        max_length=30, primary_key=True, db_index=True, verbose_name="昵称"
    )
    bobby = models.CharField(max_length=100, null=True, blank=True, verbose_name="爱好")
    created_at = models.DateField(auto_now_add=True, verbose_name="创建时间")
    update_at = models.DateField(auto_now=True, verbose_name="更新时间")

    class Meta:
        verbose_name = "助教信息"
        db_table = "courses_assistant"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.nickname
