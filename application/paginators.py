from rest_framework.pagination import PageNumberPagination


class NetworkChainPaginator(PageNumberPagination):
    """Пагинация вывода результатов"""

    page_size = 5  # Количество элементов на странице
    page_size_query_param = "page_size"  # Параметр запроса для указания количества элементов на странице
    max_page_size = 100  # Максимальное количество элементов на странице
