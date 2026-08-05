from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LoginView, CategoryViewSet, ProductViewSet

router = DefaultRouter()
router.register(r'login', LoginView, basename='login')
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'products', ProductViewSet, basename='product')

urlpatterns = [
    path('api/', include(router.urls)),
]
