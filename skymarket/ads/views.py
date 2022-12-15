from django.http import request
from requests import Response
from rest_framework import pagination, viewsets, status
from rest_framework.generics import RetrieveAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.views import APIView

from ads.models import Ad, Comment
from ads.serializers import AdSerializer, AdDetailSerializer, AdDestroySerializer, \
    AdForCurrentUserSerializer, AdListSerializer, CommentDetailSerializer, CommentDestroySerializer
from users.models import User


class AdPagination(pagination.PageNumberPagination):
    pass


# TODO view функции. Предлагаем Вам следующую структуру - но Вы всегда можете использовать свою
class AdViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.all().order_by('created_at')

    def get_serializer_class(self):
        if self.action == 'list':
            return AdListSerializer
        elif self.action == 'retrieve':
            return AdDetailSerializer
        elif self.action == 'destroy':
            return AdDestroySerializer
        elif self.action == 'partial_update':
            return AdSerializer
        elif self.action == 'create':
            return AdSerializer

    def perform_create(self, serializer):
        instance = serializer.save(author=self.request.user)
        instance = serializer.save()


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentDetailSerializer

    def perform_create(self, serializer):
        instance = serializer.save(ad=Ad.objects.get(pk=self.kwargs['ad_pk']), author=self.request.user)
        instance = serializer.save()


class CurrentCommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return CommentDetailSerializer
        elif self.action == 'destroy':
            return CommentDestroySerializer
        elif self.action == 'partial_update':
            return CommentDetailSerializer

    def get_object(self):
        return Comment.objects.get(ad_id=self.kwargs['ad_pk'], pk=self.kwargs['id'])


class MyAdAPIView(ListAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = AdForCurrentUserSerializer

    def get_queryset(self):
        user_id = self.request.user.pk
        queryset = Ad.objects.filter(author_id=user_id)
        return queryset
