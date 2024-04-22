from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import SetBoardViewSet

router = routers.SimpleRouter()
router.register(r'boards', SetBoardViewSet, 'board')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
]
