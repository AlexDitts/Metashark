from rest_framework import serializers
from .models import StudyGroup, Discipline, Direction


class StudyGroupSerializer(serializers.ModelSerializer):
    """
    Класс сериализатор для модели StudyGroup
    """
    class Meta:
        model = StudyGroup
        fields = ('number', 'discipline')


class DisciplineSerializer(serializers.ModelSerializer):
    """
    Класс сериализатор для модели Discipline
    """
    class Meta:
        model = Discipline
        fields = ('id', 'title', 'direction')


class DirectionSerializer(serializers.ModelSerializer):
    """
    Класс сериализатор для модели Direction.
    """
    class Meta:
        model = Direction
        fields = ('id', 'title', 'curator')
