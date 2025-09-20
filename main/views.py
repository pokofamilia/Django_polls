from django.shortcuts import render
# from django.http import HttpResponse

# 関数ベースビュー
# ビュー関数

from.models import Question

def index(request):
    all_question = Question.objects.all()
    context = {
        "all_question": all_question
    }
    
    return render(request, "main/index.html", context)