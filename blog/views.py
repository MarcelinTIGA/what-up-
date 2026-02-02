from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post


# Create your views here.
def post_list(request):
    posts = Post.objects.all()
    print(posts)
    return render(request, 'blog/post/list.html', {'posts': posts})


def post_detail(request, slug):
    object_list = Post.objects.all()
    Paginator = Paginator(object_list, 2)
    page = request.GET.get('page')
    try:
        posts = Paginator.page(page)
    except PageNotAnInteger:
        posts = Paginator.page(1)
    except EmptyPage:
        posts = Paginator.page(Paginator.num_pages)
        context = {
            'posts': posts, 
            'page': page,
             }
    return render(request, 'blog/post/detail.html', context)


#def post_detail(request, slug):
    post = Post.objects_or_404(Post, slug=slug)
    return render(request, 'blog/post/detail.html', {'post': post})