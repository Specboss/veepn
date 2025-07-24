from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.pagination import LimitOffsetPagination


class InfinitePagination(LimitOffsetPagination):
    default_limit = 10
    max_limit = 50


class PagePagination(PageNumberPagination):
    page_size_query_param = 'page_size'
    page_query_param = 'page'

    def get_paginated_response(self, data):
        return Response({
            'data': data,
            'paginate': {
                'page': self.page.number,
                'page_size': self.page.paginator.per_page,
                'total_pages': self.page.paginator.num_pages,
                'total_items': self.page.paginator.count,
            }
        })
