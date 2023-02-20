from django.urls import path
# from . import views
from .views import HomeView, ArticleDetailView, AddPostView, UpdatePostView, DeletePostView, AddCategoryView, CategoryView, LikeView

urlpatterns = [
    # path('', views.home, name='home'),
    path('', HomeView.as_view(), name='home'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='detail'),
    path('create/', AddPostView.as_view(), name='create'),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name='update'),
    path('article/delete/<int:pk>', DeletePostView.as_view(), name='delete'),
    path('add_category/', AddCategoryView.as_view(), name='add-category'),
    path('category/<str:cats>/', CategoryView, name='category'),
    path('like/<int:pk>', LikeView, name='like-post')

]