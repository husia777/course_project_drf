from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.generics import RetrieveAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView, UpdateAPIView

from users.models import User
from users.serializers import UserRegistrationSerializer, CurrentUserSerializer, UpdateUserSerializer, \
    UserDestroySerializer, SetPasswordSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    def get_serializer_class(self):
        if self.action == 'list':
            return CurrentUserSerializer
        elif self.action == 'retrieve':
            return CurrentUserSerializer
        elif self.action == 'destroy':
            return UserDestroySerializer
        elif self.action == 'partial_update':
            return UpdateUserSerializer
        elif self.action == 'create':
            return UserRegistrationSerializer



        return super().get_permissions()

class UserCurrentViewSet(viewsets.ModelViewSet):

    def get_serializer_class(self):
        if self.action == 'list':
            return CurrentUserSerializer
        elif self.action == 'partial_update':
            return UpdateUserSerializer

    def get_object(self):
        return self.request.user

    def get_queryset(self):
        user_id = self.request.user.pk
        queryset = User.objects.filter(pk=user_id)
        return queryset


class SetPasswordAPIView(CreateAPIView):
    queryset = User

    def get_object(self):
        return self.request.user

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = SetPasswordSerializer(data=request.data)

        if serializer.is_valid():
            current_password = serializer.data.get("current_password")
            new_password = serializer.data.get("new_password")
            if not self.object.check_password(current_password):
                return Response({current_password: ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            self.object.set_password(new_password)
            self.object.save()
            return Response({
                "new_password": new_password,
                "current_password": current_password}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
