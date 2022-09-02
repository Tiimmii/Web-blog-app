from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('posts/<str:pk>',views.posts,name='posts'),
    path('user_blog',views.user_blog,name='user_blog'),
    path('signup',views.signup,name='signup'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('search',views.search,name='search'),
    path('changes',views.changes,name='changes'),
    path('user_posts/<str:pk>',views.user_posts,name='user_posts'),
    path('edit_blog/<str:pk>',views.edit_blog,name='edit_blog'),
    path('delete_blog/<str:pk>',views.delete_blog,name='delete_blog'),
]