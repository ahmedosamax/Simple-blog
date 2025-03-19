from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Comment, Reply
from .forms import CommentForm, ReplyForm
from blog.models import BlogPost
from blog.models import Notification


def add_comment(request, post_id): 
    if request.user.is_authenticated:
        post = get_object_or_404(BlogPost, id=post_id)
        if request.method == 'POST':
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.post = post
                comment.author = request.user
                comment.save()

                # ✅ Create a notification for the post author
                if post.author != request.user:
                    Notification.objects.create(
                        user=post.author,
                        post=post,
                        comment_author=request.user,
                        message=f"{request.user.username} commented on your post: {post.title}"
                    )

                return redirect('blog_list')
        else:
            form = CommentForm()
    else:
        return redirect('login')
    return render(request, 'comments/add_comment.html', {'form': form, 'post': post})


def add_reply(request, comment_id):
    if request.user.is_authenticated:
        comment = get_object_or_404(Comment, id=comment_id)
        if request.method == 'POST':
            form = ReplyForm(request.POST)
            if form.is_valid():
                reply = form.save(commit=False)
                reply.comment = comment
                reply.author = request.user
                reply.save()

                # ✅ Create a notification for the original comment author
                if comment.author != request.user:
                    Notification.objects.create(
                        user=comment.author,
                        post=comment.post,
                        comment_author=request.user,
                        message=f"{request.user.username} replied to your comment."
                    )

                return redirect('blog_list')
        else:
            form = ReplyForm()
    else:
        return redirect('login')
    return render(request, 'comments/add_reply.html', {'form': form, 'comment': comment})