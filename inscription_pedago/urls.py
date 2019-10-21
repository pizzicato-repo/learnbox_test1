from django.urls import path

from . import test_views

urlpatterns = [
    path('', test_views.index, name='index'),
    path('create_student', test_views.create_student, name='create_student'),
]