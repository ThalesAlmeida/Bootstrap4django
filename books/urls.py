from django.urls import path
from books.views import AuthorCreate, AuthorListView, AuthorUpdate, DeleteView

urlpatterns = [
    path('author/add/', AuthorCreate.as_view(), name='author-add'),
    path('author/update/<pk>/', AuthorUpdate.as_view(), name='author-update'),
    path('author/list/', AuthorListView.as_view(), name='author-list'),
    path('author/delete/<pk>/', DeleteView.as_view(), name='author-delete'),
]