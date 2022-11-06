from rest_framework import routers
from metauniver.views import StudentViewSet
from education.views import StudyGroupApiViewSet, DirectionApiViewSet, DisciplineApiViewSet

router = routers.DefaultRouter()
router.register(r'student', StudentViewSet)
router.register(r'group', StudyGroupApiViewSet)
router.register(r'discipline', DisciplineApiViewSet)
router.register(r'direction', DirectionApiViewSet)
