from . import views
from django.urls import path


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('summernote/', include('django_summernote.urls')),
    path('', include('blog.urls'), name='blog_url')
]