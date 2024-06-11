from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


class BasicAuthViewSetMixin:
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class TokenAuthViewSetMixin:
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


class JWTAuthViewSetMixin:
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


class BasicAndTokenViewSetMixin:
    authentication_classes = BasicAuthViewSetMixin.authentication_classes + TokenAuthViewSetMixin.authentication_classes
    permission_classes = [IsAuthenticated]
