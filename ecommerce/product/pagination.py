from rest_framework.pagination import PageNumberPagination

class APIListPagination(PageNumberPagination):
    page_size = 10
    page_size_query_description = 'page_size'
    max_page_size = 1000
    limit = 20