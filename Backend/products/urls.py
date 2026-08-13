from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView
from .views import LoginView, CategoryViewSet, ProductViewSet #BrandViewSet

router = DefaultRouter()
router.register(r'login', LoginView, basename='login')
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'products', ProductViewSet, basename='product')
#router.register(r'brands', BrandViewSet, basename='brand')

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/token/refresh/',TokenRefreshView.as_view(),name='token_refresh'),
]
