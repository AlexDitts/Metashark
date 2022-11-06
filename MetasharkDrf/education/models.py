from django.db import models
from django.contrib.auth.models import User
from personnel.models import Curator


class Direction(models.Model):
    title = models.CharField(max_length=30, verbose_name='title')
    curator = models.ForeignKey(Curator,
                                null=True,
                                verbose_name='curator',
                                on_delete=models.DO_NOTHING,
                                related_name='direction',
                                )

    def __str__(self):
        return self.title


class Discipline(models.Model):
    title = models.CharField(max_length=30, verbose_name='title')
    direction = models.ForeignKey(Direction,
                                  verbose_name='direction',
                                  on_delete=models.CASCADE,
                                  related_name='discipline')

    def __str__(self):
        return self.title


class StudyGroup(models.Model):
    number = models.CharField(max_length=3, verbose_name='number')
    discipline = models.ForeignKey(Discipline,
                                   verbose_name='discipline',
                                   on_delete=models.DO_NOTHING,
                                   related_name='discipline')

    def __str__(self):
        return self.number
