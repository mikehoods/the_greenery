from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
from .forms import PostForm
from django.urls import reverse_lazy

# def home(request):
#     return render(request, 'home.html', {})

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-date']

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context

def CategoryView(request, cat):
    category_posts = Post.objects.filter(category=cat.replace('-', ' '))
    cat_menu = Category.objects.all()
    return render(request, 'categories.html', {'cat': cat.title().replace('-', ' '), 'category_posts': category_posts, 'cat_menu': cat_menu})

class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog_details.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(BlogDetailView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    # fields = ('title', 'body')

class AddCategoryView(CreateView):
    model = Category
    fields = '__all__'
    template_name = 'add_category.html'

class EditPostView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'edit_post.html'

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')