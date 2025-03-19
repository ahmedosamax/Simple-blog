from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

class BlogPost(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    video = models.FileField(upload_to='videos/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(User, related_name='blog_likes', blank=True)

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title
    
class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notifications")  # Receiver of the notification
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, null=True, blank=True)  # Post related to the notification
    comment_author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comment_notifications", null=True, blank=True)  # Who commented
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    timestamp = models.DateTimeField(default=now)

    def __str__(self):
        return f"Notification for {self.user.username}: {self.message}"

    def __str__(self):
        return f"Notification for {self.user.username} - {self.message}"


