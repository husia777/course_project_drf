from rest_framework.routers import SimpleRouter
# TODO подключите UserViewSet из Djoser.views к нашим urls.py
# TODO для этокого рекоммендуется использовать SimpleRouter
from django.urls import include, path
from rest_framework import routers

from users.models import User
from users.views import UserViewSet, UserCurrentViewSet, SetPasswordAPIView

# TODO настройка роутов для модели

router = routers.SimpleRouter()
router.register('', UserViewSet, basename=User)
# router.register('me', UserCurrentViewSet, basename=User)
urlpatterns = [
    path('me/', UserCurrentViewSet.as_view({'get': 'list', 'patch': 'partial_update'})),
    path('set_password/', SetPasswordAPIView.as_view())

]
urlpatterns += router.urls
