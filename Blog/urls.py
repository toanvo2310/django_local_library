from django.urls import path
from . import views
from .models import Post
from django.views.generic import ListView, DetailView

urlpatterns = [
    path('', views.ListView.as_view(queryset = Post.objects.all().order_by('-date'), 
                                    template_name = 'Blog/blog.html',
                                    context_object_name = 'Posts',
                                    paginate_by = 1), name = 'Blog'),

    path('<int:pk>/', views.post, name='post'),
]