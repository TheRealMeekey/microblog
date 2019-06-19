from django.shortcuts import render, redirect
from app_microblog.models import Post
from app_microblog.forms import PostForm


def post_list(request):
    if request.method == "POST":
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.save()
            return redirect('post_list')
    else:
        post_form = PostForm()
    posts = Post.objects.all().order_by('id')
    return render(request, 'app_microblog/post_list.html', {'posts': posts, 'post_form': post_form})
