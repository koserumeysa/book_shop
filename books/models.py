from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    price = models.IntegerField()
    description = models.TextField()
    created_date = models.DateField(auto_now_add=True) #It is for only one time and it will be unchanged.
    up_date = models.DateField(auto_now=True) #It will be changed every time when we update the data.
    is_published = models.BooleanField(default=False)
    cover = models.ImageField(upload_to='covers/', blank=True)

    def __str__(self):
        return f'{self.title} by {self.author}'

class Comment(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='comments')
    #name = models.CharField(max_length=200)
    name = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    up_dated = models.DateTimeField(auto_now=True)

    validation = models.PositiveIntegerField(
        validators=[MinValueValidator(1),MaxValueValidator(5)],
        )

    def __str__(self):
        return str(self.validation)