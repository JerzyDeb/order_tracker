"""Api urls."""

# Django
from django.urls import path

# 3rd-party
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView

# Project
from api.views import OrderList

schema_view = get_schema_view(
    openapi.Info(
       title='Snippets API',
       default_version='v1',
       description='Test description',
    ),
    public=True,
    permission_classes=[permissions.IsAdminUser],
)


urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-ui'),
    path('orders/', OrderList.as_view(), name='order_list'),
]
