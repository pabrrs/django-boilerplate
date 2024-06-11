from rest_framework import viewsets
from rest_framework_simplejwt.views import TokenObtainPairView as BaseTokenObtainPairView

from django_app.apps.accounts.mixins.viewsets import JWTAuthViewSetMixin
from django_app.apps.accounts.models import User
from django_app.apps.accounts.serializers import TokenObtainPairSerializer, UserSerializer

# pylint: disable=too-many-ancestors


class UserViewSet(JWTAuthViewSetMixin, viewsets.ModelViewSet):
    """
    User API
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer


class TokenObtainPairView(BaseTokenObtainPairView):
    serializer_class = TokenObtainPairSerializer
