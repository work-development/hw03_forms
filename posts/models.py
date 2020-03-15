from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Group(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(max_length=10000)

    def __str__(self):
        # выводим название группы там где на это запрос пойдет
        return self.title

class Post(models.Model):

      
    text = models.TextField()
    pub_date = models.DateTimeField("date published", auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name="posts", blank=True, null=True)

    def __str__(self):
        # выводим текст поста 
        return self.text
