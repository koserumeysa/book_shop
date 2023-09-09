from django.urls import path
from books.api import views as api_views

urlpatterns = [
    path('books/', api_views.BookListCreatorView.as_view(), name='book_list'),
]