from django.shortcuts import render
from blog.models import Post, Comment
from .forms import CommentForm

def blog_index(request):
     # query to retriev all object in the Post table
    posts = Post.objects.all().order_by('-created_on')
    #dictionary context to store all object from the query
    context = {
        "posts": posts,
    }
    return render(request, 'blog_index.html', context)

def blog_category(request, category):
    posts = Post.objects.filter(categories__name__contains=category).order_by('-created_on')
    context = {
        "category": category,
        "posts": posts
    }
    return render(request, 'blog_category.html', context)

def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)

    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author = form.cleaned_data["author"],
                body = form.cleaned_data["body"],
                post=post
            )
            comment.save()

    comments = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "comments": comments,
        "form": form,
    }
    return render(request, 'blog_detail.html', context)

# Create your views here.
