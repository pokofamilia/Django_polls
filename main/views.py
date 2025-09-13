from django.shortcuts import render
# from django.http import HttpResponse

# 関数ベースビュー
# ビュー関数
def index(request):
    question_list = [
        "人ですか",
        "あなたは僕ですか？",
        "私の母ですか？",
    ]
    context = {
        "question_list": question_list,
        "is_polled": True,
        "polled_msg": "投票誠にありがとうございました",
        "not_polled_msg": "とうひょうしてください",
        "user_name": "takasi"
    }

    
    return render(request, "main/index.html", context)


 


