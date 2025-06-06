from . import views
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
path('signup',views.signup,name = 'signup'),
path('logout/', auth_views.LogoutView.as_view(), name='logout'),   # --> لم اضع صفحة html  لأنه مجرد رابط
path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
path('password-change/', auth_views.PasswordChangeView.as_view(template_name='password_change.html'), name='password_change'),
path('password-change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'), name='password_change_done'),
path('account/',views.UserUpdateView.as_view(), name = 'my_account'),
]