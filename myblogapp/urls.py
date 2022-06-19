from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('posts/<str:pk>',views.posts,name='posts'),
    path('user_blog',views.user_blog,name='user_blog'),
    path('signup',views.signup,name='signup'),
    path('login',views.login,name='login'),
    path('search',views.search,name='search'),
    path('changes',views.changes,name='changes'),
]