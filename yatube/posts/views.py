from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post, Group, User
import datetime

def index(request):
    # одна строка вместо тысячи слов на SQL
    # latest = Post.objects.order_by('-pub_date')[:11]
    
    #author = User.objects.get(username="leo")
    #start_date = datetime.date(1854, 7, 7)
    #end_date = datetime.date(1854, 7, 21)
    #latest = Post.objects.filter(pub_date__range=(start_date, end_date)).filter(text__contains="утро").filter(author=author)

    latest = Post.objects.all()
    
    return render(request, "index.html", {"posts": latest})

def group_posts(request, slug):
    # функция get_object_or_404 позволяет получить объект из базы данных 
    # по заданным критериям или вернуть сообщение об ошибке если объект не найден
    group = get_object_or_404(Group, slug=slug)

    # Метод .filter позволяет ограничить поиск по критериям. Это аналог добавления
    # условия WHERE group_id = {group_id}
    posts = Post.objects.filter(group=group).order_by("-pub_date")[:12]
    return render(request, "group.html", {"group": group, "posts": posts})
