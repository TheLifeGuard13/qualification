import typing

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.response import Response

from application.models import NetworkChain, Product, Contact
from application.paginators import NetworkChainPaginator
from application.serializers import (
    NetworkChainSerializer,
    ProductSerializer,
    ContactSerializer,
)
from application.service import CountryFilter
from users.permissions import IsActiveStaff


class ProductViewSet(viewsets.ModelViewSet):
    """Контроллер CRUD для работы с продуктами"""

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [
        IsActiveStaff,
    ]


class ContactViewSet(viewsets.ModelViewSet):
    """Контроллер CRUD для работы с контактами"""

    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [
        IsActiveStaff,
    ]


class NetworkChainViewSet(viewsets.ModelViewSet):
    """Контроллер CRUD для работы с поставщиками/звеньями цепи"""

    queryset = NetworkChain.objects.all().order_by("id")
    serializer_class = NetworkChainSerializer
    pagination_class = NetworkChainPaginator
    filter_backends = [DjangoFilterBackend]
    filterset_class = CountryFilter
    permission_classes = [
        IsActiveStaff,
    ]

    def update(self, request: typing.Any, *args: typing.Any, **kwargs: typing.Any) -> typing.Any:
        instance = self.get_object()
        data = request.data.copy()

        # Исключаем поле 'debt_amount' из данных для обновления
        data.pop("debt_amount", None)

        serializer = self.get_serializer(instance, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)
