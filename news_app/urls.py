from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('news/', views.all_posts_page, name='all_posts_page'),
    path('news/detail/<int:pk>/', views.post_detail_page, name='post_detail_page')
]