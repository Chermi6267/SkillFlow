from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('profile/', views.home_page, name='profile'),
    path('registration/', views.registration_view, name='registration'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('password_reset/',
         auth_views.PasswordResetView.as_view(template_name="resetPassword/passwordReset.html",
                                              html_email_template_name="resetPassword/passwordResetEmail.html"),
         name='password_reset',),
    path('password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name="resetPassword/passwordResetDone.html"),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name="resetPassword/passwordResetConfirm.html"),
         name='password_reset_confirm'),
    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name="resetPassword/passwordResetComplete.html"),
         name='password_reset_complete'),
]
