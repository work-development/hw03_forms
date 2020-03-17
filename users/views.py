from django.shortcuts import render, redirect
from .forms import CreationForm
from posts.models import  User, Post
import datetime



from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import CreationForm
from posts.models import Post



class SignUp(CreateView):
        form_class = CreationForm
        success_url = "/auth/login/"
        template_name = "signup.html"

# Я часть комментариев оставил, так как хочу в будущем распечатать код и что бы остались подсказки)


