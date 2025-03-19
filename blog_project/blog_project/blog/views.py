from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import BlogPost,Notification
from .forms import BlogPostForm
from django.http import HttpResponseForbidden,JsonResponse
from django.utils.timezone import now


def blog_list(request):
    posts = BlogPost.objects.all().order_by('-created_at')
    return render(request, 'blog/blog_list.html', {'posts': posts})

@login_required
def create_blog_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            blog_post = form.save(commit=False)
            blog_post.author = request.user
            blog_post.save()
            return redirect('blog_list')
    else:
        form = BlogPostForm()
    return render(request, 'blog/create_post.html', {'form': form})

@login_required
@login_required
def edit_blog_post(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)

    if request.user != post.author:
        return redirect('blog_list')

    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES, instance=post)

        # Check if the user requested to remove the image
        if "remove_image" in request.POST and request.POST["remove_image"] == "1":
            if post.image:  # If there's an image, delete it
                post.image.delete(save=False)
                post.image = None  # Remove reference

        # Check if the user requested to remove the video
        if "remove_video" in request.POST and request.POST["remove_video"] == "1":
            if post.video:
                post.video.delete(save=False)
                post.video = None

        if form.is_valid():
            form.save()
            return redirect('blog_list')

    else:
        form = BlogPostForm(instance=post)

    return render(request, 'blog/edit_post.html', {'form': form, 'post': post})

@login_required
@login_required
def delete_blog_post(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)

    if request.user != post.author:
        return HttpResponseForbidden("You are not allowed to delete this post.")

    if request.method == 'POST':
        post.delete() 
        return redirect('blog_list')

    return render(request, 'blog/delete_post.html', {'post': post})

def like_post(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    if request.user in post.likes.all():
        post.likes.remove(request.user)  # Unlike
        liked = False
    else:
        post.likes.add(request.user)  # Like
        liked = True

    return JsonResponse({"liked": liked, "like_count": post.total_likes()})

def notifications_view(request):
    notifications = Notification.objects.filter(user=request.user, is_read=False).order_by('-timestamp')
    print(notifications)
    return render(request, 'blog/notifications.html', {'notifications': notifications})

def mark_notifications_as_read(request):
    Notification.objects.filter(user=request.user, is_read=False).update(is_read=True)
    return redirect('notifications')


def some_view(request):  # Replace 'some_view' with the correct view function
    unread_notifications = 0
    if request.user.is_authenticated:
        unread_notifications = Notification.objects.filter(user=request.user, is_read=False).count()

    return render(request, "blog/notifications.html", {
        "unread_notifications": unread_notifications
    })

def blog_detail(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    comments = post.comments.all()  # Fetch comments if you have them
    return render(request, 'blog/blog_detail.html', {'post': post, 'comments': comments})

