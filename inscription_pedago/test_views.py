from django.shortcuts import render
from django.http import HttpResponse

from inscription_pedago.models import Student, Teatcher
from django.utils import timezone


def index(request):
    return HttpResponse("Hello, world : LearnBox initiative.")

def create_student(request):
    s = Student( name="toto", inscription_date=timezone.now() )
    s.save()
    all_students = Student.objects.all()
    txt = "il y a "+ len( str(all_students)) + " students dans la base actuellement."
    return HttpResponse( 'txt' )

def test(request):
    return HttpResponse( "test" )

