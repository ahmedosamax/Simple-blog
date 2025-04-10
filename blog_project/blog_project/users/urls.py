from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('login',views.LoginPage, name='login'),
    path('register',views.RegisterPage,name='register'),
    path('home',views.HomePage,name = 'home'),
    path('logout',views.LogoutUser,name='logout'),
    path('reset_password',auth_views.PasswordResetView.as_view(template_name = 'users/password_reset.html'), name = "reset_password"),
    path('reset_password_sent',auth_views.PasswordResetDoneView.as_view(template_name = 'users/password_reset_sent.html'), name = "password_reset_done"),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name = 'users/password_reset_form.html'),name = "password_reset_confirm" ),
    path('reset_password_complete',auth_views.PasswordResetCompleteView.as_view(template_name = "users/password_reset_done.html"), name = "password_reset_complete"),
    path('pprofile', views.ProfilePage, name='profile'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

