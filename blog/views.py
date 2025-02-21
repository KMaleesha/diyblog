from django.shortcuts import render
from .models import Genre, Language, Blogger, Blog, Comment
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