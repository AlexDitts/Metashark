from django.contrib import admin
from .models import Student


class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'gender', 'group')


admin.site.register(Student, StudentAdmin)

# Register your models here.
