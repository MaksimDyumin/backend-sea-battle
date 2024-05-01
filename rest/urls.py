from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import SetBoardViewSet, UserRegisterViewSet, PlayersListViewSet, UserProfileViewSet

router = routers.SimpleRouter()
router.register(r'boards', SetBoardViewSet, 'board')


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api/v1/user/', UserRegisterViewSet.as_view({'get': 'retrieve', 'post': 'create'})),
    path('api/v1/players_list/', PlayersListViewSet.as_view({'get': 'list'})),
    path('api/v1/profile/', UserProfileViewSet.as_view({'get': 'retrieve'})),
]
