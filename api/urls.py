from django.urls import path, include
from .views import CompanyViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'companies', CompanyViewSet)
urlpatterns = [
    path('', include(router.urls))
]