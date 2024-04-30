from rest_framework import pagination
from rest_framework.response import Response


class CustomPagination(pagination.LimitOffsetPagination):
    def get_paginated_response(self, data):
        return Response(
            {
                "pagination": {
                    "next_page": self.get_next_link(),
                    "prev_page": self.get_previous_link(),
                    "total_count": self.count,
                    "offset": self.offset,
                    "limit": self.limit,
                    "default_limit": self.default_limit,
                },
                "results": data,
            }
        )


class Pagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 10000