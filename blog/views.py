from django.shortcuts import render
from .models import Post

# Create your views here.

def post_list(request):
    posts = Post.objects.all() # This line gets all the Post objects from the database using the Post model.
    return render(request, 'blog/post_list.html', {'posts': posts}) # This line renders the template blog/post_list.html with the posts obtained from the database.