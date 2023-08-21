from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
from .models import AddressInfo, Teacher, Course, Student, TeacherAssistant

# Create your views here.


class IndexView(View):
    "主页"

    def get(self, request):
        # 1. 查询、检索、过滤
        """
        objects 是模型类的对象管理器吗，如果没有更改的话，是固定写法

        .all() 是取出所有的结果

        .get() 只能返回一条结果，返回多条结果则会报错，因此传入的是主键或者唯一键作为条件
        返回过来不是字符串而是模型类

        .filter() 返回的是QuerySet集合对象，可以是多条结果
        """
        teachers1 = (
            Teacher.objects.all()
        )  # <QuerySet [<Teacher: Jack>, <Teacher: Jerry>, <Teacher: Kate>, <Teacher: Peter>]>
        print(teachers1)

        teachers2 = Teacher.objects.get(nickname="Jack")
        print(teachers2, type(teachers2))  # Jack <class 'courses.models.Teacher'>

        teachers3 = Teacher.objects.filter(fans__gte=400)  # 返回的是QuerySet集合，可以是多条结果
        for t in teachers3:
            print(f"讲师姓名{t.nickname}，粉丝数{t.fans}")
        # 讲师姓名Jack，粉丝数523
        # 讲师姓名Peter，粉丝数495

        # 2.字段数据匹配，大小写敏感
        """
        int 类型的
        xxx__gte     表示大于等于
        xxx__exact   表示刚好等于
        xxx__gt      表示大于
        xxx__in      表示在...之内
        xxx__isnull  表示是否为空
        xxx__lt      表示小于
        xxx__lte     表示小于等于
        xxx__range   表示在某某范围之内

        
        字符串类型
        xxx__contains   表示包含
        xxx__icontains  表示--- 且 （+i）大小写敏感 
        xxx__endswith   表示以...结尾
        xxx__iendswith  表示-------- 且 （+i）大小写敏感 
        ....
        """
        teachers4 = Teacher.objects.filter(fans__in=[523, 123])
        print(teachers4)  # <QuerySet [<Teacher: Jack>]>

        teachers5 = Teacher.objects.filter(fans__isnull=False)  # 表示不为空
        print(
            teachers5
        )  # QuerySet [<Teacher: Jack>, <Teacher: Jerry>, <Teacher: Kate>, <Teacher: Peter>]>

        teachers6 = Teacher.objects.filter(nickname__icontains="a")  # 表示包含a
        print(teachers6)

        # 3.结果切片、排序、链式查询
        print(Teacher.objects.all()[1:3])  # 表示从下标为1开始，取到下标为3的
        # <QuerySet [<Teacher: Jerry>, <Teacher: Kate>]>

        teachers7 = Teacher.objects.order_by("-fans")  # 表示按照fans倒序排列，默认使用升序排列（不加-）
        for t in teachers7:
            print(t.fans)

        """链式查询 就是对返回的查询集继续使用API"""
        print(
            Teacher.objects.all().filter(fans__gte=500).order_by("nickname")
        )  # <QuerySet [<Teacher: Jack>]>

        # 4.查看执行的原生SQL  print(str(xxx.query))
        print(str(teachers7.query))  # 打印出执行的原生SQL语句
        # SELECT `courses_teacher`.`nickname`, `courses_teacher`.`introduction`, `courses_teacher`.`fans`, `courses_teacher`.`created_at`, `courses_teacher`.`updated_at` FROM `courses_teacher` ORDER BY `courses_teacher`.`fans` DESC

        return render(request, "address.html")


class AddressAPIView(View):
    """地址信息"""

    def get(self, request, address_id):  # 接收一个参数的id,指mode中的pid属性对应的字段，即表中的pid_id.
        if int(address_id) == 0:  # 为0时表示为查询省，省的pid_id为null
            address_data = AddressInfo.objects.filter(pid__isnull=True).values(
                "id", "address"
            )
        else:  # 查询市或者区县
            address_data = AddressInfo.objects.filter(pid_id=int(address_id)).values(
                "id", "address"
            )
        area_list = []  # 转成list后json 序列化
        for a in address_data:
            area_list.append({"id": a["id"], "address": a["address"]})

        # 然后通过jsonResponse返回给请求方，这里是list而不是dict,所以safe需要传False
        return JsonResponse(area_list, content_type="application/json", safe=False)
