from django.urls import path
# from . import views
from .views import HomeView, BlogDetailView, AddPostView, EditPostView, DeletePostView, AddCategoryView, CategoryView

urlpatterns = [
    # path('', views.home, name='home'),
    path('', HomeView.as_view(), name='home'),
    path('blog/<int:pk>/', BlogDetailView.as_view(), name='blog-detail'),
    path('add_post/', AddPostView.as_view(), name='add-post'),
    path('blog/edit/<int:pk>/', EditPostView.as_view(), name='edit-post'),
    path('blog/<int:pk>/delete/', DeletePostView.as_view(), name='delete-post'),
    path('add_category/', AddCategoryView.as_view(), name='add-category'),
    path('category/<str:cat>/', CategoryView, name='category'),
]