from django.shortcuts import render,get_object_or_404
from .models import Post

# Create your views here.
def visample(request):
    return render(request,'blog/index.html')

def post_list(request):
    posts = Post.objects.filter(status='published')


    return render(request, 'blog/post/list.html', {'posts': posts})

def post_detail(request, year, month, day, post):
    print("post_detail")
    post = get_object_or_404(Post, slug=post,
                                   status='published',
                                   publish__year=year,
                                   publish__month=month,
                                   publish__day=day)
    print("---2--- post_detail",post)
    return render(request,'blog/post/detail.html', {'post': post})