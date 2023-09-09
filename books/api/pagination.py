from rest_framework.pagination import PageNumberPagination

class MySPagination(PageNumberPagination):
    page_size = 5

class MyLPagination(PageNumberPagination):
    page_size = 25
    page_query_param = 'page'

