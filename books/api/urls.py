from django.urls import path
from books.api import views as api_views

urlpatterns = [
    path('books/', api_views.BookListCreateAPIView.as_view(), name='book_list'),
    path('books/<int:pk>', api_views.BookDetailAPIView.as_view(), name='book_info'),
    path('books/<int:book_pk>/comments/', api_views.CommentCreateAPIView.as_view(), name='comment_create'),
    path('comments/<int:pk>', api_views.CommentDetailAPIView.as_view(), name='comment_info'),
]