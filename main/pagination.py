from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class CarPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

    def get_paginated_response(self, data):
        return Response({
            'pageCount': self.page.paginator.num_pages,  # Общее количество страниц
            'itemCount': self.page.paginator.count,  # Общее количество элементов
            'currentPage': self.page.number,  # Текущая страница
            'pageSize': self.page_size,  # Количество элементов на странице
            'results': data  # Сами данные
        })

