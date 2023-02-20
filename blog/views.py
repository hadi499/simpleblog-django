from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
from .forms import PostForm, EditForm
from django.http import HttpResponseRedirect
from django.urls import reverse

# def home(request):
#     return render(request, 'home.html')

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-id']

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'detail.html'
    def get_context_data(self, *args, **kwargs):       
        context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)
        post_like = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = post_like.total_likes()
        liked = False
        if post_like.likes.filter(id=self.request.user.id).exists():
            liked = True
        context["total_likes"] = total_likes
        context["liked"] = liked
        return context

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'create.html'
    # fields = '__all__'
   
class UpdatePostView(UpdateView):
    model = Post   
    form_class = EditForm
    template_name = 'update.html'

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete.html'
    success_url = '/'

class AddCategoryView(CreateView):
    model = Category  
    template_name = 'add_category.html'
    fields = '__all__'

def CategoryView(request, cats):
    category_posts = Post.objects.filter(category=cats.replace('-', ' '))    
    cat_menu = Category.objects.all()
    return render(request, 'categories.html', {'cats': cats.title().replace('-', ' '), 'category_posts':category_posts, 'cat_menu': cat_menu})

def LikeView(request,pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('detail', args=[str(pk)]))
