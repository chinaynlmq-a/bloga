from django import forms
from .models import Ouser
from storm.models import Article
from mdeditor.fields import MDTextFormField

class UserForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(max_length=50)
    password2 = forms.CharField(max_length=50)
    email = forms.CharField(max_length=50)


class loginForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(max_length=50)


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Ouser
        fields = ['link', 'avatar']


# 添加文章
class AddArticleForm(forms.ModelForm):
    body = MDTextFormField()
    class Meta:
        model = Article
        fields = ('title','summary','body')