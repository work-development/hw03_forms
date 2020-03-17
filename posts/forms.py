from django import forms
from posts.models import Group

class PostForm(forms.Form):
        group = forms.ModelChoiceField(required=False, queryset=Group.objects.all())
        text = forms.CharField(widget=forms.Textarea)