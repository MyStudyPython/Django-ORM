"""
函数式编程

Django原生fbv写法

思路:判断这个是什么方法,进行对应的处理
"""

# 1. 先导入json
import json

# 2. 导入JsonResponse(等同httpResponse) 返回的是Json 数据
from django.http import JsonResponse

# from django.http import httpResponse

# 4. 对于post请求需要一个 csrf 装饰器   用来解决视图可以进行跨域请求
from django.views.decorators.csrf import csrf_exempt


course_dict = {"name": "课程名称", "introduce": "课程介绍", "price": 0.11}


# 5. 装饰器写在函数的上面
@csrf_exempt
# 3.Django原生fbv写法
# 函数式编程思路:判断这个是什么方法,进行对应的处理
def course_list(request):
    if request.method == "GET":
        return JsonResponse(course_dict)
        # return httpResponse(json.dumps(course_dict), content_type="application/json")
        # json.dumps() 用于将Python对象转换为JSON格式的字符串

    if request.method == "POST":
        course = json.loads(request.body.decode("utf-8"))
        # safe=False 如果解析的数据不是字典类型 默认为true
        return JsonResponse(course, safe=False)
        # return httpResonse(json.dumps(course), content_type="application/json")


"""
类视图

Django CBV写法

思路:对不同的请求方法用对应的函数处理
"""

from django.views import View
from django.utils.decorators import method_decorator


# 注意是双骆驼 两个单词首字母都大写
# 类视图的编程思路:对不同的请求方法用对应的函数处理


# 2. 在函数体上加 method_decorator
# name 指请求方式,dispatch 的原理是因为django 请求相应决定的,先进入dispatch,再进入post
@method_decorator(csrf_exempt, name="dispatch")
class CourseList(View):
    def get(self, request):
        return JsonResponse(course_dict)

    # 1.直接在post 上加 csrf_exempt装饰器
    # @csrf_exempt
    def post(self, request):
        course = json.loads(request.body.decode("utf-8"))
        return JsonResponse(course, safe=False)


"""
问题是 如果是用django 原生写接口的话,有很多东西都需要自己从零开始实现

比如说分页、数据排序、接口认证、接口权限、接口的限流

这些需求算是一个restful api接口的标配
于是就有了drf视图 集成了这些接口开发常用功能
"""
