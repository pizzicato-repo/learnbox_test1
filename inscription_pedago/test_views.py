from django.shortcuts import render
from django.http import HttpResponse

from inscription_pedago.models import Student, Teatcher
from django.utils import timezone

from django.shortcuts import render, get_object_or_404

def create_student(request):
    s = Student( name="toto", inscription_date=timezone.now() )
    s.save()
    all_students = Student.objects.all()
    txt = "il y a "+ str( len(all_students)) + " students dans la base actuellement."
    return HttpResponse( txt )

def test(request):
    return render(request, 'inscription_pedago/base.html', {})

def test_simple(request):
    return render(request, 'inscription_pedago/simple.html', {})

def menu1(request):
    return render(request, 'inscription_pedago/menu1.html', {})

def inscription(request):
    return render(request, 'inscription_pedago/b_inscription.html', {})

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
        return render(request, 'inscription_pedago/student_edit.html', {'form': form})


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

class StudentCreate(CreateView):
    model = Student
    fields = ['student_name']
    template_name_suffix = '_edit'
    # success_url = "/campaigns/list" => get_absolute_url
    
    def form_valid(self, form):
        form.instance.inscription_date = timezone.now()
        return super().form_valid(form)

class StudentDetail(DetailView):
    model = Student
    template_name = 'inscription_pedago/student-detail.html'