from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('category/  <slug:category>/', views.post_list, name='category_posts_list'),
    path('post/<slug:slug>/', views.post_detail, name='post_detail'),
]