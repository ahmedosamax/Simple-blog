from django.urls import path
from . import views

urlpatterns = [
    path('add/<int:post_id>/', views.add_comment, name='add_comment'),
    path('reply/<int:comment_id>/', views.add_reply, name='add_reply'),
]
