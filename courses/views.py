from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
from .models import AddressInfo, Teacher, Course, Student, TeacherAssistant

# 导入需要用的函数
from django.db.models import Count, Avg, Max, Min, Sum

# Create your views here.


class IndexView(View):
    "主页"

    # def get(self, request):
    #     # 1. 查询、检索、过滤
    #     """
    #     objects 是模型类的对象管理器吗，如果没有更改的话，是固定写法

    #     .all() 是取出所有的结果

    #     .get() 只能返回一条结果，返回多条结果则会报错，因此传入的是主键或者唯一键作为条件
    #     返回过来不是字符串而是模型类

    #     .filter() 返回的是QuerySet集合对象，可以是多条结果
    #     """
    #     teachers1 = (
    #         Teacher.objects.all()
    #     )  # <QuerySet [<Teacher: Jack>, <Teacher: Jerry>, <Teacher: Kate>, <Teacher: Peter>]>
    #     print(teachers1)

    #     teachers2 = Teacher.objects.get(nickname="Jack")
    #     print(teachers2, type(teachers2))  # Jack <class 'courses.models.Teacher'>

    #     teachers3 = Teacher.objects.filter(fans__gte=400)  # 返回的是QuerySet集合，可以是多条结果
    #     for t in teachers3:
    #         print(f"讲师姓名{t.nickname}，粉丝数{t.fans}")
    #     # 讲师姓名Jack，粉丝数523
    #     # 讲师姓名Peter，粉丝数495

    #     # 2.字段数据匹配，大小写敏感
    #     """
    #     int 类型的
    #     xxx__gte     表示大于等于
    #     xxx__exact   表示刚好等于
    #     xxx__gt      表示大于
    #     xxx__in      表示在...之内
    #     xxx__isnull  表示是否为空
    #     xxx__lt      表示小于
    #     xxx__lte     表示小于等于
    #     xxx__range   表示在某某范围之内

    #     字符串类型
    #     xxx__contains   表示包含
    #     xxx__icontains  表示--- 且 （+i）大小写敏感
    #     xxx__endswith   表示以...结尾
    #     xxx__iendswith  表示-------- 且 （+i）大小写敏感
    #     ....
    #     """
    #     teachers4 = Teacher.objects.filter(fans__in=[523, 123])
    #     print(teachers4)  # <QuerySet [<Teacher: Jack>]>

    #     teachers5 = Teacher.objects.filter(fans__isnull=False)  # 表示不为空
    #     print(
    #         teachers5
    #     )  # QuerySet [<Teacher: Jack>, <Teacher: Jerry>, <Teacher: Kate>, <Teacher: Peter>]>

    #     teachers6 = Teacher.objects.filter(nickname__icontains="a")  # 表示包含a
    #     print(teachers6)

    #     # 3.结果切片、排序、链式查询
    #     print(Teacher.objects.all()[1:3])  # 表示从下标为1开始，取到下标为3的
    #     # <QuerySet [<Teacher: Jerry>, <Teacher: Kate>]>

    #     teachers7 = Teacher.objects.order_by("-fans")  # 表示按照fans倒序排列，默认使用升序排列（不加-）
    #     for t in teachers7:
    #         print(t.fans)

    #     """链式查询 就是对返回的查询集继续使用API"""
    #     print(
    #         Teacher.objects.all().filter(fans__gte=500).order_by("nickname")
    #     )  # <QuerySet [<Teacher: Jack>]>

    #     # 4.查看执行的原生SQL  str(xxx.query)
    #     print(str(teachers7.query))  # 打印出执行的原生SQL语句
    #     # SELECT `courses_teacher`.`nickname`, `courses_teacher`.`introduction`, `courses_teacher`.`fans`, `courses_teacher`.`created_at`, `courses_teacher`.`updated_at` FROM `courses_teacher` ORDER BY `courses_teacher`.`fans` DESC

    #     return render(request, "address.html")

    # def get(self, request):
    #     """
    #     返回新的QuerySet API

    #     1. all(),        查询所有数据
    #        filter(),     返回满足条件的对象
    #        order_by(),   根据某个字段进行排序
    #        exclude(),    根据输入的某个条件排除
    #        reverse(),    反向排序
    #                      一定在Meta中设置`ordering`,多个ordering的时候取第一个
    #                      默认按照关键字的顺序输出
    #                      更改此项不需要重新生成数据表
    #        distinct()   去重

    #     2. extra(),     实现字段别名
    #        defer(),     排除一些字段
    #        only()       选择一些字段
    #        字段相关API

    #     3. values()     获取字典  形式的QuerySet
    #        values_list  获取元组  形式的QuerySet
    #                     flat:将单个字段的数据直接放到列表里面  只限于获取单个数据的信息

    #     4. dates(),     年月日
    #        datetimes()  年月日时分秒
    #        根据时间日期获取查询集

    #     5. union() / | ,              并集
    #        intersection()/ &,         交集
    #        difference()               差集

    #     6. select_related()     一对一，多对一查询优化，
    #        prefetch_related()   一对多，多对多查询优化，
    #        反向查询

    #        查询优化API

    #     7. annodate()  使用聚合计数、求和、平均数
    #                    聚合就是分组

    #        raw()       执行原生的SQL

    #     """

    #     #  1.all()  filter()  order_by():排序  exclude():除了xx元素以外  reverse():反向排序  distinct():去重
    #     # 使用exclude 排除某一项
    #     s1 = Student.objects.all().exclude(nickname="A同学")
    #     for s in s1:
    #         # print(s.nickname, s.age)
    #         pass

    #     # 使用reverse 反向排序
    #     s2 = Student.objects.all().exclude(nickname="A同学").reverse()
    #     for s in s2:
    #         # print(s.nickname, s.age)
    #         pass

    #     # 2.extra():给字段取别名   defer():排除一些字段   only():选择一些字段
    #     # extra(): extra(select={"[要取的别名]": "[原来字段名]"})
    #     s3 = Student.objects.all().extra(select={"name": "nickname"})
    #     for s in s3:
    #         # print(s.name, s.age)
    #         pass

    #     # print(
    #     #     str(Student.objects.all().only("nickname", "age").query)
    #     # )  # SELECT `courses_student`.`nickname`, `courses_student`.`age` FROM `courses_student` ORDER BY `courses_student`.`age` ASC

    #     # 3.values():字典 values_list():元组  获取字典或者是元组形式的queryset
    #     # values() 输出的是dict类型的
    #     # print(TeacherAssistant.objects.values("nickname", "hobby"))
    #     # <QuerySet [{'nickname': '助教1', 'hobby': '看老友记'}, {'nickname': '助教2', 'hobby': '看生活大爆炸'}, {'nickname': '助教3', 'hobby': '看小鲤鱼历险记'}]>
    #     # values_list() 输出的是元组类型的数据
    #     # print(TeacherAssistant.objects.values_list("nickname", "hobby"))
    #     # <QuerySet [('助教1', '看老友记'), ('助教2', '看生活大爆炸'), ('助教3', '看小鲤鱼历险记')]>
    #     # flat:将单个字段的数据直接放到列表里面  只限于获取单个数据的信息
    #     # print(TeacherAssistant.objects.values_list("nickname", flat=True))
    #     # <QuerySet ['助教2', '助教3', '助教1']>

    #     """
    #     4.根据时间和日期获取查询集
    #     dates:年月日
    #     datetimes年月日时分秒查询字段多一点有时分秒
    #     使用什么查询方式取决于定义字段的类型
    #     """
    #     # dates('[查询日期的字段]', '查询是 year month day', order='是降序DESC 升序ASC(默认) ')
    #     # print(Course.objects.dates("created_at", "month", order="DESC"))
    #     # <QuerySet [datetime.date(2023, 8, 1), datetime.date(2023, 7, 1), datetime.date(2023, 6, 1)]>
    #     # datetimes('[查询时间的字段]', 'month', order='DESC')
    #     # print(Course.objects.datetimes("created_at", "month", order="DESC"))

    #     # 5.集合的运算  union():并集   intersection():交集   difference():差集
    #     s1 = Course.objects.filter(price__gte=240)  # 大于等于240
    #     s2 = Course.objects.filter(price__lte=260)  # 小于等于260

    #     # print(s1.union(s2))  # 并集
    #     # print(s1.intersection(s2))  # 交集
    #     # print(s1.difference(s2))  # 差集
    #     """
    #     低版本的MySQL 不支持 intersection 和  difference，目前版本支持
    #     """
    #     # print(s1 | s2)  # 并集
    #     # print(s1 & s2)  # 交集
    #     # print(s1 - s2)  # 差集
    #     # print(s1 + s2)  # 并集
    #     # unsupported operand type(s) for - / + : 'QuerySet' and 'QuerySet' 不支持

    #     """
    #     6.优化查询api
    #     select_related()     一对一 多对一的优化查询
    #     prefetch_related()   一对多 多对多的优化查询
    #     反向查询

    #     """
    #     # course = Course.objects.all()  # 查询课程表
    #     # for c in course:
    #     #     print(f"{c.title}--{c.teacher.nickname}--{c.teacher.fans}")
    #     """
    #     查询优化
    #     {c.teacher.nickname}--{c.teacher.fans} 是通过外键关联查询 需要把每一条SQL语句输出出来

    #     需要配置项目的settings文件 配置日志，终端可以输出所有的debug 信息

    #     输出之后发现通过teacher外键关联的时候 又去查询了这个表 无意增加了数据库查询压力

    #     用select_related() 减少查询次数来减少数据库查询效率
    #     """
    #     # 通过课程获取讲师信息 查询相关信息通过外接字段进行连接
    #     course = Course.objects.all().select_related("teacher")  # 查询课程表的同时查询老师表
    #     for c in course:
    #         # print(f"{c.title}--{c.teacher.nickname}--{c.teacher.fans}")
    #         pass

    #     # student = Student.objects.filter(age__lt=30)
    #     student = Student.objects.filter(age__lt=30).prefetch_related(
    #         "course"
    #     )  # 查询学生信息表的同时查询课程表
    #     for s in student:
    #         # print(s.course.all())
    #         pass

    #     """反向查询：根据父表查询子表"""
    #     # print(Teacher.objects.get(nickname="Jack").course_set.all())
    #     """
    #     如果在关联的外键上设置 `related_name`

    #     course_set ----> teac (设置 `related_name` 的值)
    #     """
    #     # print(Teacher.objects.get(nickname="Jack").teac.all())

    #     # 7.annotate() 使用聚合计数、求和、平均数、raw()、执行原生的SQL
    #     """
    #     我们以讲师来分组,每一个讲师所有课程销量的总和,以及他的平均价格
    #     """
    #     # 总和
    #     print(Course.objects.values("teacher").annotate(vol=Sum("volume")))
    #     # 平均
    #     print(Course.objects.values("teacher").annotate(pri=Avg("price")))
    #     # raw() 就是执行SQL原生语句

    #     return render(request, "address.html")

    def get(self, request):
        """
        不返回新的QuerySet API

        1. 获取对象
           get()               获取对象
           get_or_create()     有数据就通过get获取没有就创建数据
           first()             第一条记录
           last()              最后一条记录
           lastest()           最近的记录
           earliest()          最早的记录
           in_bulk()           批量返回对象

        2. 创建对象
           create()             创建
           bulk_create()        批量创建
           update_or_create()   创建或更新

        3. 更新对象
           update()             更新
           update_or_create()   更新或创建

        4. 删除对象
           delete()            删除(使用filter过滤)

        5. 其他操作
           exists()            判断是否存在
           count()             统计个数
           aggregate()           聚合


        """
        """1.获取对象 get() get_or_create() first() last()  latest()  earliest()  in_bulk()"""
        # first() 第一条记录
        # print(Course.objects.first())  # 打印格式为 {type} - {title}
        # last()  最后一条记录
        # print(Course.objects.last())

        # 需要在模型类里面设置 get_latest_by = [创建的字段] 代表根据创建的字段进行排序
        # latest()  # 最近的记录
        # print(Course.objects.latest())
        # earliest() # 最早的记录
        # print(Course.objects.earliest())

        # in_bulk() 批量返回对象 根据主键的值传递一个列表 列表中传递主键的值
        # print(Course.objects.in_bulk(["Python 课程系列2", "PHP进阶课程1"]))  # 返回一个字典

        """2.创建对象  create():创建对象  bulk_create():批量创建对象  create_or_update():如果没有就创建有就更新"""
        # bulk_create:给函数传一个列表

        """3.更新对象 update():更新  update_or_create():更新或创建"""
        # update
        Course.objects.filter(title="Python 课程系列1").update(price=1000)

        """ 4.删除对象 delete():使用filter过滤"""
        Course.objects.filter(title="test").delete()

        """5.其他操作 exist():是否存在  count():统计个数  aggregate():聚合"""
        # exist():是否存在
        # print(Course.objects.filter(title="test").exists())  # False
        # print(Course.objects.filter(title="Python 课程系列1").exists())  # True

        # count():记录数据表中的数据个数
        # print(Course.objects.count())  # 21 数据库的记录数

        # annotate():和value配合使用 对分组结果进行统计
        # aggregate():对整个数据库中的数据结果进行处理

        # 对整个课程找出最大值，最小值，平均值，总和进行统计
        print(
            Course.objects.aggregate(
                Max("price"), Min("price"), Avg("price"), Sum("volume")
            )
        )
        # {'price__max': 1000, 'price__min': 220, 'price__avg': 479.9524, 'volume__sum': 78302}

        # 字段名是 "字段__函数名"

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
