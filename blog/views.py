from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post
from django.views.generic import ListView

# Create your views here.
def visample(request):
    return render(request,'blog/index.html')

def post_list1(request):
    posts = Post.objects.filter(status='published')
    # posts = Post.publish.all()
    return render(request, 'blog/post/list.html', {'posts': posts})

def post_list(request):
    object_list = Post.objects.filter(status='published')
    paginator = Paginator(object_list, 3)  # 3 posts in each page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)
    return render(request,
                  'blog/post/list.html',
                  {'page': page,
                   'posts': posts})

class PostListView(ListView):
    queryset = Post.objects.filter(status='published')
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'

def post_detail(request, year, month, day, post):
    print("post_detail")
    post = get_object_or_404(Post, slug=post,
                                   status='published',
                                   publish__year=year,
                                   publish__month=month,
                                   publish__day=day)
    print("---2--- post_detail",post)
    return render(request,'blog/post/detail.html', {'post': post})