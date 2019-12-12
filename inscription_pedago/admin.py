from django.contrib import admin

# Register your models here.
from .models import Student, Teatcher, Discipline, Validation_code, ContactModel

# admin.site.register(Student)
# admin.site.register(Teatcher)
# admin.site.register(Discipline)
# admin.site.register(Validation_code)

admin.site.register(ContactModel)