import django_filters
from django_filters.rest_framework import FilterSet

from application.models import NetworkChain


def clear_debt(modeladmin, request, queryset):
    """
    Очищает задолженность выбранных поставщиков.
    """
    queryset.update(debt_amount=0)
    return queryset


class CountryFilter(FilterSet):
    """
    Фильтр по стране контакта.
    """
    country = django_filters.CharFilter(field_name='contact__country', lookup_expr='icontains')

    class Meta:
        model = NetworkChain
        fields = ["country"]
