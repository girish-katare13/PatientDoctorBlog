from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm,BlogPostForm
from .models import BlogPost
from django.http import JsonResponse

def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST,request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
            user = form.save()
            login(request, user)
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

@login_required(login_url="login")
def dashboard_view(request):
    user = request.user
    return render(request, 'dashboard.html', {'user': user})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def create_blog_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            blog_post = form.save(commit=False)
            blog_post.author = request.user
            blog_post.save()
            return redirect('dashboard')  # Change this to wherever you want to redirect after posting
    else:
        form = BlogPostForm()
    return render(request, 'create_blog_post.html', {'form': form})

@login_required
def view_blog_posts(request):
    if request.user.user_type == 'doctor':
        blog_posts = BlogPost.objects.filter(author=request.user)
    else:  # If user is not a doctor, show all posts
        blog_posts = BlogPost.objects.exclude(is_draft=True)
    return render(request, 'view_blog_posts.html', {'blog_posts': blog_posts})

@login_required
def blog_posts_api_view(request):
    category = request.GET.get('category', None)
    user = request.user

    if user.user_type == 'doctor':
        blog_posts = BlogPost.objects.filter(author=user)
    elif category:
        blog_posts = BlogPost.objects.filter(category__name=category, is_draft=False)
    else:
        blog_posts = BlogPost.objects.filter(is_draft=False)

    data = [{'title': post.title, 'image': post.image.url, 'summary': post.summary} for post in blog_posts]
    return JsonResponse(data, safe=False)