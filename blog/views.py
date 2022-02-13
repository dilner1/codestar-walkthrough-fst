from django.shortcuts import render
from django.views import generic, View
from .models import Post

# Create your views here.
class PostList(generic.ListView):
    model = Post
    query_set = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6

class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1).order_by('-created_on')
        tenplate_name = 'index.html'
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approve=True).order_by('created_on')
