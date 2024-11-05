from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404

# Create your views here.

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date') # This line gets all the Post objects from the database using the Post model.
    return render(request, 'blog/post_list.html', {'posts': posts}) # This line renders the template blog/post_list.html with the posts obtained from the database.

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})