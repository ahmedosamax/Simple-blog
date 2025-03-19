from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Notification
from comments.models import Comment

@receiver(post_save, sender=Comment)
def send_comment_notification(sender, instance, created, **kwargs):
    if created:
        post = instance.post
        if post.author != instance.author:  # Don't notify if the author comments on their own post
            Notification.objects.create(
                user=post.author,
                post=post,
                comment_author=instance.author,
                message=f"{instance.author.username} commented on your post: {post.title}"
            )