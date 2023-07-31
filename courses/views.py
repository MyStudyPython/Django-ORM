from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
from .models import AddressInfo

# Create your views here.


class IndexView(View):
    "主页"

    def get(self, request):
        return render(request, "index.html")


class AddressAPIView(View):
    """地址信息"""

    def get(self, request, address_id):  # 接收一个参数的id,指mode中的pid属性对应的字段，即表中的pid_id.
        if int(address_id) == 0:  # 为0时表示为查询省，省的pid_id为null
            address_data = AddressInfo.objects.filter(pid_isnull=True).valuse(
                "id", "address"
            )
        else:  # 查询市或者区县
            address_data = AddressInfo.objects.filter(pid_id=int(address_id)).valuse(
                "id", "address"
            )
        area_list = []  # 转成list后json 序列化
        for a in address_data:
            area_list.append({"id": a["id"], "address": a["address"]})

        # 然后通过jsonResponse返回给请求方，这里是list而不是dict,所以safe需要传False
        return JsonResponse(area_list, content_type="application/json", safe=False)
