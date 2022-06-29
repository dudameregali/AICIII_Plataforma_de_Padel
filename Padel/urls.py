
from django.contrib import admin
from django.urls import path, include
from cadastro.api.views import CadastroViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'cadastro', CadastroViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
