from celery.result import AsyncResult
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import StudyGroup, Direction, Discipline
from rest_framework import viewsets
from .permissions import AdministratorPermission, CuratorPermission
from .serializers import StudyGroupSerializer, DisciplineSerializer, DirectionSerializer
from .tasks import report_task
from django.core.cache import cache


class StudyGroupApiViewSet(viewsets.ModelViewSet):
    """
    Класс представление для отображения списка групп студентов, а также для добавления, удаления и редактирования групп.
    Доступен только пользователю, состоящему в группе куратор.
    """
    queryset = StudyGroup.objects.all()
    serializer_class = StudyGroupSerializer
    permission_classes = (CuratorPermission, )


class DisciplineApiViewSet(viewsets.ModelViewSet):
    """
        Класс представление для отображения списка дисциплин, а также для добавления, удаления и редактирования групп.
        Доступен только пользователю, состоящему в группе Администратор.
        """
    queryset = Discipline.objects.all()
    serializer_class = DisciplineSerializer
    permission_classes = (AdministratorPermission, )


class DirectionApiViewSet(viewsets.ModelViewSet):
    """
    Класс представление для отображения списка групп студентов, а также для добавления, удаления и редактирования групп.
    Доступен только пользователю, состоящему в группе куратор.
    """
    queryset = Direction.objects.all()
    serializer_class = DirectionSerializer
    permission_classes = (AdministratorPermission, )


class StartReportApiView(APIView):
    """
    Класс представление для запуска процедуры создания эксель-файла отчёта.
    Доступен только пользователю, состоящему в группе администратор.
    """
    permission_classes = (AdministratorPermission, )

    def get(self, request):
        """
        Метод для запуска для запуска процедуры создания эксель-файла отчёта в фоновом режиме. После запуска процедуры
        """
        result = report_task.delay()
        return Response({'message': 'Начат процесс создания отчёта.',
                         'task_id': result.id})


class GetStatusTaskApiView(APIView):
    """
    Класс представление для проверки статуса выполнения процедуры создания отчёта.
    Доступен только пользователю, состоящему в группе администратор.
    """
    permission_classes = (AdministratorPermission, )

    def get(self, request):
        task_id = cache.get('task_id')
        if task_id:
            res = AsyncResult(task_id)
            return Response(res.state)
        return Response({'message': 'Выполняемых задач нет'})
