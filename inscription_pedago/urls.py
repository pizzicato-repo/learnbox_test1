from django.urls import path

from . import test_views

urlpatterns = [
    path('base_v2', test_views.base_v2, name='base_v2'),

    path('base', test_views.base, name='base'),
    #test redirections
    path('', test_views.menu1, name='menu1'),
        
    path('student/new/', test_views.student_new, name='student_new'),
    #path('student/create/', test_views.StudentCreate.as_view(), name='student_create'),
    
    path('student/<int:pk>/detail/', test_views.StudentDetail.as_view(), name='student-detail'),
    path('student/<int:pk>/edit/', test_views.student_edit, name='student_edit'),
    
    path('ask_codes/', test_views.ask_codes, name='ask_codes'),
    path('validate_codes/<int:pk>/', test_views.validate_codes, name='validate_codes'),

    path('teatcher/<int:pk>/', test_views.TeatcherDetail.as_view(), name='teatcher_detail'),
    
    path('test_mail', test_views.test_mail, name='test_mail'),
    path('instrument', test_views.instrument, name='instrument'),

    # path('contact', test_views.contact, name='contact'), #OK
    path('contact', test_views.ContactCreate.as_view(), name='contact'), #OK

    path('will_contact', test_views.will_contact, name='will_contact'),
]
