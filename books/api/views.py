from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin

from rest_framework import generics
from rest_framework.generics import get_object_or_404

from books.models import Book, Comment
from books.api.serializers import CommentSerializer, BookSerializer

class BookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

#We dont need to specify any pk because GenericAPIView already knows that we are going to use a pk.
class BookDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class CommentCreateAPIView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        book_pk = self.kwargs.get('book_pk')
        #If there is a book with the id, it will return it. If not, it will return 404.
        book = generics.get_object_or_404(Book, pk=book_pk)
        #It has a related object as a book. That's why, we can give the book.
        serializer.save(book=book)

class CommentDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer        

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