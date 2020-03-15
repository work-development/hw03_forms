from django.shortcuts import render, redirect
from .forms import CreationForm
from posts.models import  User, Post
import datetime


# Create your views here.
# позволяет узнать ссылку на URL по его имени, параметр name функции path
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import CreationForm
from .forms import PostForm
from posts.models import Post
from django.shortcuts import redirect


class SignUp(CreateView):
        form_class = CreationForm
        success_url = "/auth/login/"
        template_name = "signup.html"

def new_post(request):
        if request.method == 'POST':
                form = PostForm(request.POST)
                if form.is_valid():
                        Post.objects.create(author=request.user, text=form.cleaned_data['text'], group = form.cleaned_data['group'])
                        #p.save()
                        latest = Post.objects.all()
                        #return render(request,'index.html',{'form':latest})
                        return redirect('/') 
        form = PostForm()
        return render(request,'new.html',{'form':form})


