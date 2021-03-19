from .models import Profile
from django  import forms
from django.contrib.auth.models import User
from blog.models import Post



class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields=['username','email']

class PofileUpdateForm(forms.ModelForm):
    # email=forms.EmailField(max_length=200)
    class Meta:
        model = Profile
        fields =['image']

class CreatePost(forms.ModelForm):
    class Meta:
        model =Post
        fields =['title','content']