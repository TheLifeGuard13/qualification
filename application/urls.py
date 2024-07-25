from rest_framework.routers import DefaultRouter

from application.apps import ApplicationConfig
from application.views import NetworkChainViewSet, ProductViewSet, ContactViewSet

app_name = ApplicationConfig.name

network_router = DefaultRouter()
network_router.register(r"network", NetworkChainViewSet, basename="network")

product_router = DefaultRouter()
product_router.register(r"product", ProductViewSet, basename="product")

contact_router = DefaultRouter()
contact_router.register(r"contact", ContactViewSet, basename="contact")


urlpatterns = [] + network_router.urls + product_router.urls + contact_router.urls
