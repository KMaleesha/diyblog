from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), 
    path('blogs/', views.BlogListView.as_view(), name='blogs'),
    path('blogs/<int:pk>', views.BlogDetailView.as_view(), name='blog-detail'),
    path('blogs/<int:blog_id>/create/', views.add_comment, name='add_comment'),
    path('bloggers/', views.BloggerListView.as_view(), name='bloggers'),
    path('bloggers/<int:pk>', views.BloggerDetailView.as_view(), name='blogger-detail'),
]