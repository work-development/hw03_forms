import datetime
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CreationForm
from posts.models import  User, Post

#  Здесь вроде два пробела должно быть?
class SignUp(CreateView):
        form_class = CreationForm
        success_url = "/auth/login/"
        template_name = "signup.html"

# "...А коммитить код без них" Вы имеете ввиду сохранить у себя на компе две версии 
# проекта и в одной (для себя) все комментить а вторую (пустую, без комментов) отправлять на праверку?

# Сейчас оставил только важные комментарии



