from django.shortcuts import render
from .models import Blogger, Blog, Comment
from django.views import generic

def index(request):
    """View function for home page of site."""

    num_blogs = Blog.objects.all().count()
    num_authors = Blogger.objects.count()
    num_visits = request.session.get('num_visits', 0)
    num_visits += 1
    request.session['num_visits'] = num_visits

    context = {
        'num_blogs': num_blogs,
        'num_authors': num_authors,
        'num_visits': num_visits,
    }

    return render(request, 'index.html', context=context)

class BlogListView(generic.ListView):
    model = Blog
    paginate_by = 5

class BlogDetailView(generic.DetailView):
    model = Blog

class BloggerListView(generic.ListView):
    model = Blogger

class BloggerDetailView(generic.DetailView):
    model = Blogger


    
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Blog, Comment
from .forms import CommentForm

@login_required
def add_comment(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.blog = blog
            comment.commenter = request.user 
            comment.save()
            return redirect('blog-detail', pk=blog.id)
    
    else:
        form = CommentForm()
    
    return render(request, 'blog/add_comment.html', {'form': form, 'blog': blog})
