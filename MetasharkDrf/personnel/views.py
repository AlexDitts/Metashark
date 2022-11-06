from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer


class UserDetailApiView(generics.RetrieveUpdateAPIView):
    """
    Класс представление вывода данных пользователя. Пользователь берётся из request.user
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_object(self):
        obj = self.request.user
        return obj
