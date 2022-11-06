from django.db import models
from django.core.validators import MinValueValidator
from rest_framework.exceptions import ValidationError
from education.models import StudyGroup


class Student(models.Model):
    """
    Модель объекта "Студент".
    """
    GENDER = (
        (0, 'male'),
        (1, 'female')
    )
    name = models.CharField(max_length=30, verbose_name='name')
    age = models.IntegerField(verbose_name='age', validators=[MinValueValidator(16, message='to low age')])
    gender = models.CharField(choices=GENDER, verbose_name='gender', max_length=6)
    group = models.ForeignKey(StudyGroup,
                              verbose_name='group',
                              on_delete=models.DO_NOTHING,
                              related_name='student')

    def save(self, *args, **kwargs):
        """
        Метод save переопределён для ограничения количества записей в одной группе не больше 20.
        Перед сохранением записи в БД метод проверяет количество студентов (объектов модели) в одной группе
        При попытке сохранить 21ю запись в одну группу вызывается исключение ValidationError. Вызванное исключение далее
        обрабатывается представлением.
        :param args:
        :param kwargs:
        :return: None
        """
        quantity = self.__class__.objects.filter(group_id=self.group_id).count()
        print(quantity)
        if quantity > 20:
            raise ValidationError('Превышено количество студентов в группе')
        super().save()

    def __str__(self):
        return self.name
