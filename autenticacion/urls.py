from django.urls import path
from .views import PruebaProtegida, LoginJSON, RegistroJSON
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('login-json/', LoginJSON.as_view(), name='login_json'),
    path('registro-json/', RegistroJSON.as_view(), name='registro_json'),
    path('protegido/', PruebaProtegida.as_view(), name='prueba_protegida'),
] 