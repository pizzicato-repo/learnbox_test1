from django.urls import path

from . import test_views

urlpatterns = [
    path('', test_views.index, name='index'),
]