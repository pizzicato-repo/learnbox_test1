from django.shortcuts import render
from django.http import HttpResponse

from inscription_pedago.models import Student, Teatcher, Validation_code
from django.utils import timezone

from django.shortcuts import render, get_object_or_404

# def create_student(request):
#     s = Student( name="toto", inscription_date=timezone.now() )
#     s.save()
#     all_students = Student.objects.all()
#     txt = "il y a "+ str( len(all_students)) + " students dans la base actuellement."
#     return HttpResponse( txt )

def base(request):
    return render(request, 'inscription_pedago/base.html', {})

def menu1(request):
    temp = request.META.get('HTTP_REFERER', None)
    return render(request, 'inscription_pedago/menu1.html', {'temp' : temp})

from .forms import StudentForm
from django.shortcuts import redirect

def student_new(request):        
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)

            student.inscription_date = timezone.now()
    
            student.save()
            return redirect('student-detail', pk=student.pk)
        else:
            print("form not valide")
    else:
        form = StudentForm()

        temp = request.META.get('HTTP_REFERER', None)
        return render(request, 'inscription_pedago/student_edit.html', {'form': form, 'temp':temp})

def student_edit(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            student = form.save(commit=False)
            student.inscription_date = timezone.now()
            student.save()
            return redirect('student-detail', pk=student.pk)
    else:
        form = StudentForm(instance=student)
    return render(request, 'inscription_pedago/student_edit.html', {'form': form})

from django.views.generic.edit import CreateView
from django.views.generic import DetailView

# TODO : get_context_data
# class StudentCreate(CreateView):
#     model = Student
#     fields = ['name', 'surname', 'email', 'date_of_birth']
#     template_name_suffix = '_edit'
#     # success_url = "/campaigns/list" => get_absolute_url
    
#     def form_valid(self, form):
#         form.instance.inscription_date = timezone.now()
#         return super().form_valid(form)

class StudentDetail(DetailView):
    model = Student
    template_name = 'inscription_pedago/student-detail.html'

import random

def get_code():
    ch = ''
    for i in range(12) :
        k = random.randrange(1, 35)
        if k<10 :
            ch += str(k)
        else:
            ch += chr( 65 + k - 10 )
    return ch   

def ask_codes(request):
    dico = {'teatchers' : Teatcher.objects.all() }
    return render(request, 'inscription_pedago/ask_codes.html', dico)

def validate_codes(request, pk):
    teatcher = Teatcher.objects.get(pk=pk)

    codes = [  ]
    for i in range(4):
        str_code = get_code()
        is_already = Validation_code.objects.filter(code=str_code).count() != 0
        if not is_already :
            code = Validation_code(code=str_code, teatcher=teatcher)
            code.save()
            codes.append( str_code )

    #names_teatchers = [ str(teatcher) for teatcher in Teatcher.objects.all() ]
    # print( 'names_teatchers', names_teatchers )
    dico = {'codes' : codes, 'teatcher' : teatcher }
    return render(request, 'inscription_pedago/validate_codes.html', dico)