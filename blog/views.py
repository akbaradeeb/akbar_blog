# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse,HttpResponseRedirect,Http404
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import auth,messages
from .models import Blog,Comment,Profile
from .forms import SignUpForm,CommentForm,BlogForm,UpdateProfileForm

# Create your views here.
def index(request):
    posts = Blog.objects.filter(status=1).order_by('-created_at')[:10]
    return render(request,'blog/index.html',{'posts':posts})

def detail(request, mid=None, slug=None):
    try:
        post = Blog.objects.get(url=slug)
        post_comments = Comment.objects.filter(blog_id=post.id).order_by('-created_at')
        form = CommentForm()
    except Blog.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'blog/detail.html', {'post': post,'post_comments':post_comments,'comment_form':form})

def login(request):
    if request.user.is_authenticated():
        return redirect('/')

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/');
        else:
            messages.error(request,"Error wrong username/password")

    return  render(request,'blog/login.html')

def logout(request):
    auth.logout(request)
    return redirect('/');
    return render(request,'blog/logout.html')

def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if(form.is_valid()):
            user = form.save()
            user.refresh_from_db()
            user.profile.birth_date = form.cleaned_data.get('birth_date')
            user.save()

            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username,password = raw_password)
            login(request,user)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request,'blog/signup.html',{'form': form})

def post_comment(request):
    if request.is_ajax():
        form = CommentForm(request.POST)
        if form.is_valid():
            blog    = Blog.objects.get(id=request.POST['blog_id'])
            comment = form.save(blog)
            #comment.refresh_from_db()
            #comment.save()
            return render(request, 'blog/post_comment.html', {'comment':comment})
    else:
        return render(request, 'blog/post_comment.html')

def profile(request):
    return render(request, 'blog/profile.html',{})

def profile_update(request):
    profile = get_object_or_404(Profile,pk=request.user.profile.id)

    if request.method == "POST":
        form = UpdateProfileForm(request.POST or None, request.FILES,instance=profile)
        if(form.is_valid()):
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            #return redirect('/')
    else:
        form = UpdateProfileForm(instance=profile)
    return render(request, 'blog/profile_update.html',{'form':form})

def add_blog(request):
    if request.method == "POST":
        form = BlogForm(request.POST)
        if(form.is_valid()):
            blog = form.save(user=request.user)
            return redirect('/')
    else:
        form = BlogForm()
    return render(request, 'blog/add_blog.html',{'form':form})

def profile_blogs(request):
    status = {1:'Enable',2:'Disable'}
    blogs = Blog.objects.filter(author=request.user.id).order_by('-created_at')
    return render(request, 'blog/profile_blogs.html', {'blogs': blogs,'status':status})

def edit_blog(request,id=None):
    blog = get_object_or_404(Blog, pk=id)
    if request.method == "POST":
        form = BlogForm(request.POST or None, request.FILES,instance=blog)
        if(form.is_valid()):
            update_blog = form.save(user=request.user,create_slug=False,commit=False)
            update_blog.url = blog.url
            update_blog.save()
            return redirect('/')
    else:
        form = BlogForm(instance=blog)
    return render(request, 'blog/edit_blog.html',{'form':form})