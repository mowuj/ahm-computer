from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .import views
router = DefaultRouter()

router.register('', views.AddToCartViewSet)
router.register('order', views.OrderViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
