from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post, Group, User
from .forms import PostForm
import datetime
from django.shortcuts import redirect


def index(request):
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

def new_post(request):
        if request.method == 'POST':
                form = PostForm(request.POST)
                if form.is_valid():
                        Post.objects.create(author=request.user, text=form.cleaned_data['text'], group = form.cleaned_data['group'])
                        return redirect("/") 
        form = PostForm()
        return render(request,'new.html',{'form':form})
