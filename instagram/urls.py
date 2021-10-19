from django.conf.urls import url
from django.urls import re_path,path
from django.contrib.auth import views as auth_views
from . import views as app_views
from . import views


urlpatterns = [
    path('index/',views.index,name='home'),

    path('accounts/register/',app_views.register,name='register'),
    path('',auth_views.LoginView.as_view(template_name = 'registration/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name = 'registration/logout.html'),name='logout'),
    path('accounts/profile/',views.profile,name='profile'),
    path('update/',app_views.update_profile,name='update_profile'),
    path('post/',app_views.post,name='post'),
    path('photo/<int:photo_id>',views.detail,  name='photo.detail'),
]