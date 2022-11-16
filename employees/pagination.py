from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


DEFAULT_PAGE = 1
DEFAULT_PAGE_SIZE = 3

class CustomPagination(PageNumberPagination):
    page = DEFAULT_PAGE
    page_size = DEFAULT_PAGE_SIZE

    def get_id(self, data):
        new = []
        for item in data:
            new.append(item['id'])
        if not new:
            new = [0, 0]
        return new

    def get_paginated_response(self, data):
        return Response({
            'data': data,
            'meta': {
                'current_page': int(self.request.GET.get('page', DEFAULT_PAGE)),
                'page_size': int(self.request.GET.get('page_size', self.page_size)),
                'last_page': self.page.paginator.num_pages,
                'total': self.page.paginator.count,
                'from': min(self.get_id(data)),
                'to': max(self.get_id(data)),
            },
        })