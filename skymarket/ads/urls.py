from django.urls import include, path
from rest_framework import routers

from ads.models import Ad
from ads.views import AdViewSet, MyAdAPIView, CommentViewSet, CurrentCommentViewSet

# TODO настройка роутов для модели

router = routers.SimpleRouter()
router.register('', AdViewSet, basename=Ad)
urlpatterns = [
    path('me/', MyAdAPIView.as_view()),
    path('<int:ad_pk>/comments/<int:id>/',
         CurrentCommentViewSet.as_view({'get': 'retrieve', 'patch': 'partial_update', 'delete': 'destroy'})),
    path('<int:ad_pk>/comments/', CommentViewSet.as_view({'get': 'list', 'post': 'create'}))

]
urlpatterns += router.urls
