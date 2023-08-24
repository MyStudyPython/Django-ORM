from django.contrib import admin

# 导入模型类
from .models import Course

# Register your models here.


# Django 框架中用于注册模型（Model）到管理后台的装饰器
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    # list_display 需要显示的字段
    list_display = ("name", "introduction", "teacher", "price")

    # search_fields 需要搜索的字段
    search_fields = list_display

    # list_filter 需要过滤的字段
    list_filter = list_display

    # list_editable 可编辑的字段
    # style_fields 在编辑视图中的显示效果 形如css
