from django.contrib import admin
from education.models import Direction, Discipline, Curator, StudyGroup


class CuratorAdmin(admin.ModelAdmin):
    list_display = ('id', 'phone')


class StudyGroupAdmin(admin.ModelAdmin):
    list_display = ('number', 'discipline')


class DirectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


class DisciplineAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'direction')


admin.site.register(Direction, DirectionAdmin)
admin.site.register(Discipline, DisciplineAdmin)
admin.site.register(Curator, CuratorAdmin)
admin.site.register(StudyGroup, StudyGroupAdmin)
# Register your models here.
