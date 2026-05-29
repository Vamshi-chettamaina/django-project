from django.contrib import admin
from app1.models import student
# Register your models here.

class student_admin(admin.ModelAdmin):
    list_display=['sid','sname','age','course']
    ordering=['sid']

admin.site.register(student,student_admin)