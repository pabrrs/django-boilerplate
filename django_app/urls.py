"""django_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import RedirectView
from health_check import urls as health_check_urls
from rest_framework import routers
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView

from django_app.apps.accounts.viewsets import TokenObtainPairView, UserViewSet

# JWT-protected /api endpoints
apiRouter = routers.DefaultRouter()
apiRouter.register(r"users", UserViewSet)

# Basic-protected /integration endpoint
integrationRouter = routers.DefaultRouter()

# Admin customization
admin.site.site_title = "Django App"
admin.site.site_header = "Django App"
admin.site.index_title = "Contrate Quem Luta"

urlpatterns = [
    path("health/", include(health_check_urls)),
    path("admin/", admin.site.urls),
    path("", RedirectView.as_view(url="api/", permanent=False)),
    # API
    path("api/", include(apiRouter.urls)),
    # Integration
    path("integration/", include(integrationRouter.urls)),
    # JWT
    path("api/login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/token/verify/", TokenVerifyView.as_view(), name="token_verify"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
