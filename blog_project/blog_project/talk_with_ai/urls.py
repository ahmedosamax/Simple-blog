from django.urls import path
from .views import chat_with_ai, chat_page

urlpatterns = [
    path("", chat_page, name="chat_page"),
    path("chat/", chat_with_ai, name="chat_with_ai"),
]