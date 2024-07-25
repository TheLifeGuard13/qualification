from django.contrib import admin

from application.models import Product, Contact, NetworkChain
from application.service import clear_debt


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "model",
        "market_date",
        "seller",
    )
    search_fields = ("name",)
    list_filter = (
        "market_date",
        "seller",
    )


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = (
        "email",
        "country",
        "city",
        "street",
        "building",
        "seller",
    )
    search_fields = ("email",)
    list_filter = (
        "country",
        "city",
    )


@admin.register(NetworkChain)
class NetworkChainAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "supplier",
        "debt_amount",
        "created",
    )
    search_fields = (
        "name",
        "supplier",
        "debt_amount",
        "created",
    )
    list_filter = (
        "name",
        "supplier",
    )
    actions = [clear_debt]
