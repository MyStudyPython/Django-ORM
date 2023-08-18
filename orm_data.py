import os
import sys
import random
import django
from datetime import date

project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_path)  # 将项目路径添加到系统搜寻路径当中
os.environ["DJANGO_SETTINGS_MODULE"] = "imooc.settings"  # 设置项目的配置文件
django.setup()  # 初始化django环境


from courses.models import Teacher, Course, Student, TeacherAssistant


def import_data():
    """
    使用 Django ORM 导入数据
    """

    # 讲师数据 create()
    Teacher.objects.create(nickname="老王", introduction="Python 工程师", fans=666)
    Teacher.objects.create(nickname="老张", introduction="Java 工程师", fans=123)
    Teacher.objects.create(nickname="老李", introduction="Golang 工程师", fans=888)

    # 课程数据 bulk_create() -- 批量导入数据
    Course.objects.bulk_create(
        [
            Course(
                title=f"Python 课程系列{i}",
                teacher=Teacher.objects.get(nickname="老王"),
                type=random.choice((0, 1, 2)),
                price=random.randint(200, 300),
                volume=random.randint(100, 10000),
                online=date(2018, 10, 4),
            )
            for i in range(1, 5)
        ]
    )

    Course.objects.bulk_create(
        [
            Course(
                title=f"Java 课程系列{i}",
                teacher=Teacher.objects.get(nickname="老张"),
                type=random.choice((0, 1, 2)),
                price=random.randint(200, 300),
                volume=random.randint(100, 10000),
                online=date(2018, 6, 4),
            )
            for i in range(1, 4)
        ]
    )

    Course.objects.bulk_create(
        [
            Course(
                title=f"Golang 课程系列{i}",
                teacher=Teacher.objects.get(nickname="老李"),
                type=random.choice((0, 1, 2)),
                price=random.randint(200, 300),
                volume=random.randint(100, 10000),
                online=date(2018, 1, 1),
            )
            for i in range(1, 3)
        ]
    )

    # 学生数据 update or create()
    # update or create() - 把主键或者具有唯一键特性的字段放在外面，其他的字段放在defaults里面
    Student.objects.update_or_create(
        nickname="小A",
        defaults={
            "age": random.randint(18, 58),
            "gender": random.choice((0, 1, 2)),
            "study_time": random.randint(9, 999),
        },
    )

    Student.objects.update_or_create(
        nickname="小B",
        defaults={
            "age": random.randint(18, 58),
            "gender": random.choice((0, 1, 2)),
            "study_time": random.randint(9, 999),
        },
    )

    Student.objects.update_or_create(
        nickname="小C",
        defaults={
            "age": random.randint(18, 58),
            "gender": random.choice((0, 1, 2)),
            "study_time": random.randint(9, 999),
        },
    )

    Student.objects.update_or_create(
        nickname="小D",
        defaults={
            "age": random.randint(18, 58),
            "gender": random.choice((0, 1, 2)),
            "study_time": random.randint(9, 999),
        },
    )

    # 添加外键字段
    # 正向添加
    # 销量大于等于1000的课程
    Student.objects.get(nickname="小A").course.add(
        *Course.objects.filter(volume__gte=1000)
    )
    # 销量大于5000的课程
    Student.objects.get(nickname="小B").course.add(
        *Course.objects.filter(volume__gt=5000)
    )

    # 反向添加
    # 学习时间大于等于500小时的同学
    Course.objects.get(title="Python 课程系列1").student_set.add(
        *Student.objects.filter(study_time__gte=500)
    )
    # 学习时间小于等于500小时的同学
    Course.objects.get(title="Python 课程系列2").student_set.add(
        *Student.objects.filter(study_time__lte=50)
    )

    # 助教数据 get_or_create()
    TeacherAssistant.objects.get_or_create(
        nickname="助教1",
        defaults={"hobby": "看老友记", "teacher": Teacher.objects.get(nickname="老王")},
    )
    TeacherAssistant.objects.get_or_create(
        nickname="助教2",
        defaults={"hobby": "看生活大爆炸", "teacher": Teacher.objects.get(nickname="老张")},
    )
    TeacherAssistant.objects.get_or_create(
        nickname="助教3",
        defaults={"hobby": "看小鲤鱼历险记", "teacher": Teacher.objects.get(nickname="老李")},
    )


# 判断当前脚本是否作为主程序直接运行，而在被导入时不会执行
if __name__ == "__main__":
    # 在此处写入希望在直接执行模块时被执行的代码
    if import_data():
        print("数据导入成功！")
