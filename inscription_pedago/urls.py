from django.urls import path

from . import test_views

urlpatterns = [
    path('test', test_views.test, name='test'),
    path('create_student', test_views.create_student, name='create_student'),
    path('', test_views.index, name='index'),
]
