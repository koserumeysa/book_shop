from rest_framework import serializers
from books.models import Book, Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        #fields = '__all__'
        #We exclude book because we only want to change the related book in the url.
        exclude = ['book',] 

class BookSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    class Meta:
        model = Book
        fields = '__all__'

