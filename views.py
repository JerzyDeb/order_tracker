"""Api views."""

# 3rd-party
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt import authentication

# Project
from .utils import get_serializer_class, get_model_objects


class OrderList(ListAPIView):  # noqa: D101
    authentication_classes = [authentication.JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = get_serializer_class()

    def get_queryset(self):
        user = self.request.user
        return get_model_objects(user)
