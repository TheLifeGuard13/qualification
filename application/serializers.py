from rest_framework import serializers

from application.models import Product, Contact, NetworkChain


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"


class NetworkChainSerializer(serializers.ModelSerializer):
    products = ProductSerializer(source="product_set", many=True, read_only=True)
    contacts = ContactSerializer(source="contact_set", many=True, read_only=True)

    class Meta:
        model = NetworkChain
        fields = "__all__"
