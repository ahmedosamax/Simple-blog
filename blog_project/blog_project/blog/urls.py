from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_list, name='blog_list'),
    path('create/', views.create_blog_post, name='create_blog_post'),
    path('edit/<int:post_id>/', views.edit_blog_post, name='edit_blog_post'),
    path('delete/<int:post_id>/', views.delete_blog_post, name='delete_blog_post'),
    path('post/<int:post_id>/', views.blog_detail, name='blog_detail'),
    path('post/<int:post_id>/like/', views.like_post, name='like-post'),
    path('notifications/', views.notifications_view, name='notifications'),
    path('notifications/read/', views.mark_notifications_as_read, name='mark_notifications_as_read'),
]
