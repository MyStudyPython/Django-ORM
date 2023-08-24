from django.db import models
from django.conf import settings

# Create your models here.


class Course(models.Model):
    """
    CharField 基本类型字段
    max_length 设置字段为255，
    unique 课程名称唯一
    help_text 字段的注解或者表单校验提示信息
    """

    name = models.CharField(
        max_length=255, unique=True, help_text="课程名称", verbose_name="名称"
    )

    """
  TextField 不限制长度
  """
    introduction = models.TextField(help_text="课程介绍", verbose_name="介绍")

    """
  settings.AUTH_USER_MODEL 关联到认证用户的模型类 也就是user表
  on_delete 删除级联
  """
    teacher = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        help_text="课程讲师",
        verbose_name="讲师",
    )

    """
  max_digits 总长度 6位
  decimal_places 小数两位
  """
    price = models.DecimalField(
        max_digits=6, decimal_places=2, help_text="课程介绍", verbose_name="介绍"
    )

    """
  创建时间自动添加
  """
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    # 元数据 ---<这里会显示中文>
    class Meta:
        verbose_name = "课程信息"
        # 复数也是一样
        verbose_name_plural = verbose_name
        # 增加一个排序
        ordering = ("price",)

    # 模型类实例
    def __str__(self):
        return self.name


# Course.objects.all()  # Django QuerySet 或者 生成模型类实例的时候 instance
