from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin

from rest_framework import generics
from rest_framework.generics import get_object_or_404
from rest_framework import permissions
from rest_framework.exceptions import ValidationError

from books.models import Book, Comment
from books.api.serializers import CommentSerializer, BookSerializer
from books.api.permissions import IsAdminUserOrReadOnly, IsCommenterOrReadOnly
from books.api.pagination import MySPagination, MyLPagination

class BookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminUserOrReadOnly]
    pagination_class = MySPagination

#We dont need to specify any pk because GenericAPIView already knows that we are going to use a pk.
class BookDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminUserOrReadOnly]

class CommentCreateAPIView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAdminUserOrReadOnly]

    def perform_create(self, serializer):
        book_pk = self.kwargs.get('book_pk')
        #If there is a book with the id, it will return it. If not, it will return 404.
        book = generics.get_object_or_404(Book, pk=book_pk)
        user = self.request.user
        comments = Comment.objects.filter(book=book, commenter=user)
        if comments.exists():
            raise ValidationError('You have already commented on this book.')
        #It has a related object as a book. That's why, we can give the book.
        serializer.save(book=book, commenter=user)

class CommentDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer 
    permission_classes = [IsCommenterOrReadOnly]       

#We dont need to use all of these. We can do everything with the above class.
# class BookListCreatorView(ListModelMixin, CreateModelMixin, GenericAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
    
#     #List all books
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     #Create a new book
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)