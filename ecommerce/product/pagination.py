from rest_framework.pagination import PageNumberPagination

class ProductAPIListPagination(PageNumberPagination):
    page_size = 3
    page_size_query_description = 'page_size'
    max_page_size = 1000