from django.urls import path
from django.contrib.auth.views import LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.LandingPageView.as_view(), name='landing'),
    path('feed/', views.FeedView.as_view(), name='feed'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(
        next_page='core:landing',
        http_method_names=['get', 'post']
    ), name='logout'),
    
    # Password Reset URLs
    path('password-reset/', PasswordResetView.as_view(
        template_name='core/auth/password_reset.html',
        email_template_name='core/auth/password_reset_email.html',
        subject_template_name='core/auth/password_reset_subject.txt'
    ), name='password_reset'),
    path('password-reset/done/', PasswordResetDoneView.as_view(
        template_name='core/auth/password_reset_done.html'
    ), name='password_reset_done'),
    path('password-reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(
        template_name='core/auth/password_reset_confirm.html'
    ), name='password_reset_confirm'),
    path('password-reset/complete/', PasswordResetCompleteView.as_view(
        template_name='core/auth/password_reset_complete.html'
    ), name='password_reset_complete'),
] 