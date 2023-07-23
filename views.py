"""Api views."""


# Django
from django.conf import settings

# 3rd-party
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt import authentication

# Project
from api.utils import get_serializer_class, get_model_objects
from shop.models import Order


class OrderList(ListAPIView):  # noqa: D101
    authentication_classes = [authentication.JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = get_serializer_class()

    def get_queryset(self):
        user = self.request.user
        return get_model_objects(user)
