from django.contrib import admin
from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = (
        'student_id',
        'first_name',
        'last_name',
        'email',
        'department',
        'year',
    )

    search_fields = (
        'student_id',
        'first_name',
        'last_name',
        'email',
    )

    list_filter = (
        'department',
        'year',
        'gender',
    )

    ordering = ('student_id',)