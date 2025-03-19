from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm , UserUpdateForm, ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.decorators import login_required
from blog.models import BlogPost

def RegisterPage(request):
    if request.user.is_authenticated:
        return redirect('blog_list')
    else:
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Welcome ' + user)
            return redirect('login')
        context = {'form':form}
        return render(request, 'users/register.html',context)

def LoginPage(request):
    if request.user.is_authenticated:
        return redirect('blog_list')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username = username , password = password)
            if user is not None:
                login(request , user)
                return redirect('blog_list')
            else:
                messages.info(request, 'Username OR password incorrect')
                return render (request,'users/login.html')
        return render (request,'users/login.html')

def LogoutUser(request):
    logout(request)
    return redirect ('login')
@login_required(login_url='login')
def HomePage(request):
    return render (request, 'users/home.html')

@login_required
def ProfilePage(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    user_blogs = BlogPost.objects.filter(author=request.user)  # Fetch user blogs

    context = {
        'u_form': u_form,
        'p_form': p_form,
        'user_blogs': user_blogs,  # Pass blogs to template
    }
    return render(request, 'users/profile.html', context)


