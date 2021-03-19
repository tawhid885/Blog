from django import forms
from .models import Post, Category

choices=Category.objects.all().values_list('name','name')

choice_list=[]
for item in choices:
    choice_list.append(item)

class PostForm(forms.ModelForm):
    class Meta:
        model =Post
        fields =('title','content','category')

        widgets ={
            'title':forms.TextInput(),
            'content':forms.TextInput(),
            'category':forms.Select(choices=choice_list),
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model =Category
        fields='__all__'

        widgets={
            'name':forms.TextInput(),
        }