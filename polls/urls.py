from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # polls/というURLがリクエストされたら、mainのurls.pyを参照
    path("polls/", include("main.urls")),
]
