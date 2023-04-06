from django.shortcuts import render, redirect, get_object_or_404
from .models import *


# Create your views here.
def home(request):
    posts = Post.objects.all()
    return render(request,'home.html',{'posts':posts})

def detail(request,post_id):
    post_detail = get_object_or_404(Post,pk=post_id)
    return render(request, 'detail.html',{'post':post_detail})

def create(request):
  if request.method=="POST":
    post = Post()
    post.title = request.POST['title']
    post.body = request.POST['body']
    post.date = timezone.now()
    try:
        post.image = request.FILES['image']
    except:
        post.image = None
    post.save()
    return redirect('/detail/'+str(post.id),{'post':post})
  else:
    post = Post()
    return render(request,'create.html',{'post':post})


def update(request, post_id):
  post = Post.objects.get(id=post_id)
  if request.method == "POST":
    post.title = request.POST['title']
    post.body = request.POST['body']
    post.date = timezone.now()
    try:
      post.image = request.FILES['image']
    except:
      post.image = None
    post.save()
    return redirect('/detail/'+str(post.id),{'post':post})
  else:
    post=Post()
    return render(request, 'update.html', {'post':post})

def delete(request, post_id):
  post = Post.objects.get(id=post_id)
  post.delete()
  return redirect('home')

def detail(request,post_id):
  post_detail = get_object_or_404(Post,pk=post_id)
  comments = Comment.objects.filter(post = post_id)
  if request.method == "POST":
    comment = Comment()
    comment.post = post_detail
    comment.body = request.POST['body']
    comment.date = timezone.now()
    comment.save()
  return render(request,'detail.html',{'post':post_detail, 'comments':comments})
