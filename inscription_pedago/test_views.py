from django.shortcuts import render
from django.http import HttpResponse

from inscription_pedago.models import Student, Teatcher
from django.utils import timezone

from django.shortcuts import render

def create_student(request):
    s = Student( name="toto", inscription_date=timezone.now() )
    s.save()
    all_students = Student.objects.all()
    txt = "il y a "+ str( len(all_students)) + " students dans la base actuellement."
    return HttpResponse( txt )

def test(request):
    return render(request, 'inscriptions_pedago/base.html', {})

def test_simple(request):
    return render(request, 'inscriptions_pedago/simple.html', {})

def menu1(request):
    return render(request, 'inscriptions_pedago/menu1.html', {})

def inscription(request):
    return render(request, 'inscriptions_pedago/inscription.html', {})

def b_all(request):
    return render(request, 'inscriptions_pedago/b_all.html', {})
