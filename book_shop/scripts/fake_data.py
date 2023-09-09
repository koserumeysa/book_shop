import os
import random
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'book_shop.settings')

import django
django.setup()

from django.contrib.auth.models import User
from faker import Faker
import requests

def set_user():
    fake = Faker('en-US')

    f_name = fake.first_name()
    l_name = fake.last_name()
    u_name = f'{f_name.lower()}{l_name.lower()}'
    email = f'{u_name}@{fake.domain_name()}'
    print(f_name, l_name, email)

    user_check = User.objects.filter(username=u_name)
    while user_check.exists():
        u_name = u_name + str(random.randrange(1, 99))


    user = User(
        username = u_name,
        first_name = f_name,
        last_name = l_name,
        email = email,
    )

    user.set_password('testing321..')
    user.save()

from books.api.serializers import BookSerializer

def find_book(topic):
    fake = Faker('en-US')
    url = 'https://openlibrary.org/search.json'
    payload = {'q': topic}
    response = requests.get(url, params=payload)

    if response.status_code != 200:
        print('You requested in a wrong way.', response.status_code)
        return
    
    json_data = response.json()
    book_list = json_data.get('docs')
    
    for book in book_list:
        book_name = book.get('title')
        data = dict(
            name = book_name,
            author = book.get('author_name')[0],
            #description = '-'.join(book.get('text')),
            published_date = fake.date_time_between(start_date='-10y', end_date='now', tzinfo=None),
        )
        serializer = BookSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            print('Book is saved:', book_name)
        else:
            continue #if there is an error in data, it can continue.


    

