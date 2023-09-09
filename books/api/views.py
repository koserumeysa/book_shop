from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin


from books.models import Book, Comment
from books.api.serializers import CommentSerializer, BookSerializer

class BookListCreatorView(ListModelMixin, CreateModelMixin, GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    #List all books
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    #Create a new book
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)