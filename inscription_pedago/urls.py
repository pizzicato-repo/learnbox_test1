from django.urls import path

from . import test_views

urlpatterns = [
    path('base', test_views.base, name='base'),
    #test redirections
    path('menu1', test_views.menu1, name='menu1'),
        
    # almost same job
    path('student/new/', test_views.student_new, name='student_new'),
    path('student/create/', test_views.StudentCreate.as_view(), name='student_create'),
    
    path('student/<int:pk>/detail/', test_views.StudentDetail.as_view(), name='student-detail'),
    path('student/<int:pk>/edit/', test_views.student_edit, name='student_edit'),
    
    path('ask_codes/', test_views.ask_codes, name='ask_codes'),
    path('validate_codes/<int:pk>/', test_views.validate_codes, name='validate_codes'),
]
