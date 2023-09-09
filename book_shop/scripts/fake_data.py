import os
import random
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'book_shop.settings')

import django
django.setup()

from django.contrib.auth.models import User
from faker import Faker

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