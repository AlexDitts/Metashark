from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from education.permissions import CuratorPermission


class StudentListPagination(PageNumberPagination):
    """
    Класс пагинатор для представления списка студентов
    """
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 50


class StudentViewSet(viewsets.ModelViewSet):
    """
    Класс представление для вывода списка студентов, а так же для добавления новых, редактирования и удаления
    существующих.
    """
    queryset = Student.objects.all().order_by('group')
    serializer_class = StudentSerializer
    permission_classes = (CuratorPermission, )
    pagination_class = StudentListPagination
