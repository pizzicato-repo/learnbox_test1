from django.urls import path

from . import test_views

urlpatterns = [
    path('test', test_views.test, name='test'),
    path('test_simple', test_views.test_simple, name='test_simple'),

    path('menu1', test_views.menu1, name='menu1'),
    
    path('create_student', test_views.create_student, name='create_student'),
    
    path('inscription', test_views.inscription, name='inscription'),
    path('', test_views.b_all, name='b_all'),
]
