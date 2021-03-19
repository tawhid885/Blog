from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User, auth, Group
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import PofileUpdateForm, UserUpdateForm
from django.contrib import messages


def home(request):
    return render(request,'accounts/home.html')

@login_required
def profile(request):
    if request.method == "POST":
        u_form =UserUpdateForm(request.POST,instance=request.user)
        p_form =PofileUpdateForm(request.POST, request.FILES, instance = request.user.profile)
        

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            username = u_form.cleaned_data.get('username')
            messages.success(request,f'successfully updated {username} profile!')
            return redirect('profile')

        
    else:
        u_form =UserUpdateForm(instance=request.user)
        p_form = PofileUpdateForm(instance = request.user.profile)

    context ={'u_form':u_form,
            'p_form':p_form}
    return render(request,'accounts/profile.html',context)
    

def register(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username = username).exists():
                print('username already taken')
            else:
                user = User.objects.create_user(first_name = firstname ,last_name = lastname ,username=username,email= email, password = password1)
                print('username is taken')
                user.save()
                group = Group.objects.get(name='Editor')
                user.groups.add(group)
        else:
            print('password did not match')

        return redirect('login')
    else:
        return render(request,'accounts/register.html')




