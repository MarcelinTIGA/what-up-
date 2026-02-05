from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post, Comment
from .forms import CommentForm


# Create your views here.

def post_list(request):
    object_list = Post.objects.all()
    paginator = Paginator(object_list, 2)
    page = request.GET.get('page')

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {
        'posts': posts,
        'page': page,
    }

    return render(request, 'blog/post/list.html', context)


def post_detail(request, slug: str):
    post = get_object_or_404(Post, slug=slug)
    comments = Comment.objects.filter(post=post.id)
    new_comment = None
    if request.method == 'POST':
        comment_form = CommentForm(data= request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, 'blog/post/detail.html', {
                                        'post': post, 
                                        'comments': comments, 
                                        'new_comment': new_comment, 
                                        'comment_form': comment_form 
                                        })