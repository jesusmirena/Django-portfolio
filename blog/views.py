from django.shortcuts import get_object_or_404, render
from .models import Post


def render_posts(request):
    posts = Post.objects.all()
    context = {"posts": posts}
    return render(request, "posts.html", context)


def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    context = {"post": post}
    return render(request, "post_detail.html", context)
