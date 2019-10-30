from django.contrib import admin

# Register your models here.
from .models import Student, Teatcher, Discipline

admin.site.register(Student)
admin.site.register(Teatcher)
admin.site.register(Discipline)