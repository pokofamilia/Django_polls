from django.shortcuts import render
from django.http import HttpResponse

# 関数ベースビュー
# ビュー関数
def index(request):
    return HttpResponse("光る10万円pcがどうしても欲しい")
 


# def greet(request, name):
#     massage = "こんにちは" + name + "さん!!"
#     return HttpResponse(massage)

