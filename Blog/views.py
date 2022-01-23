from django.shortcuts import render, get_object_or_404
from .models import Post, Comment
from django.views.generic import ListView, DetailView
from Blog.forms import CommentForm
from django.http import HttpResponseRedirect

# Create your views here.
'''
def List(request):
    Data = {'Posts': Post.objects.all().order_by('-date')}
    return render(request, 'Blog/blog.html', Data)


class Post_List_View(ListView):

    queryset = Post.objects.all().order_by('-date')
    template_name = 'Blog/blog.html'
    context_object_name = 'Posts'
    paginate_by = 1 # Maximum number of posts


def post(request, id):
    try:
        detail = Post.objects.get(id=id)
    except Post.DoesNotExist:
        raise "Page not found 404"

    return render(request, 'Blog/post.html', {'detail': detail})


class post_Detail_View(DetailView):
    model = Post
    template_name = 'Blog/post.html'
'''

def post(request, pk):

    post = get_object_or_404(Post, pk=pk)
    form = CommentForm()
    
    if request.method == 'POST':
        form = CommentForm(request.POST, author = request.user, post = post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.path)

    return render(request, 'Blog/post.html', {'post': post, 'form': form})