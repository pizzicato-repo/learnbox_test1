from django.urls import path

from . import test_views

urlpatterns = [
    path('test', test_views.test, name='test'),
    path('test_simple', test_views.test_simple, name='test_simple'),

    path('menu1', test_views.menu1, name='menu1'),
    
    # path('create_student', test_views.create_student, name='create_student'),
    
    path('inscription', test_views.inscription, name='inscription'),

    # same job
    path('student/new/', test_views.student_new, name='student_new'),
    path('student/create/', test_views.StudentCreate.as_view(), name='student_create'),
    
    path('student/<int:pk>/detail/', test_views.StudentDetail.as_view(), name='student-detail'),
    path('student/<int:pk>/edit/', test_views.student_edit, name='student_edit'),

]
