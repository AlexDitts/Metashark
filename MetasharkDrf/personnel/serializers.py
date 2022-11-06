from rest_framework import serializers
from personnel.models import Curator
from django.contrib.auth.models import User


class CuratorSerializer(serializers.ModelSerializer):
    """
    Сериализатор модели куратора.
    """
    class Meta:
        model = Curator
        fields = ('id', 'name')


class UserSerializer(serializers.ModelSerializer):
    """
    Сериализатор модели пользователя. Для удобства прочтения, группа пользователя выводится не как id и по названию
    группы.
    """
    groups = serializers.StringRelatedField(many=True)

    class Meta:
        model = User
        fields = '__all__'
        read_only_fields = [
            'groups',
            'is_active',
            'is_staff',
            'password',
            'user_permissions',
            'date_joined',
            'is_superuser',
        ]
