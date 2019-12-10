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

def display_message(request, message):    
    return render(request, 'inscription_pedago/message.html', {'message': message})

def base(request):
    return render(request, 'inscription_pedago/base.html', {})


def base_v2(request):
    return render(request, 'inscription_pedago/base_v2.html', {})


def menu1(request):
    temp = request.META.get('HTTP_REFERER', None)
    return render(request, 'inscription_pedago/menu1.html', {'temp' : temp})

from .forms import StudentForm
from django.shortcuts import redirect


def student_new(request): 
    if request.method == "POST":
        sent_code = request.session['sent_code']

        #url_sender = request.META.get('HTTP_REFERER', 'None')
        form = StudentForm(request.POST)
        if form.is_valid():
            if sent_code is None : 
                return display_message(request, "Votre code d'inscription n'a pas été récupéré à partir du site du prof, veuillez nous contacter.")
            else :
                current_code = Validation_code.objects.get(code=sent_code)
                if current_code is None : 
                    return display_message(request, "Votre code d'inscription n'existe pas.")
                else :                    
                    if current_code.student is None :
                        student = form.save(commit=False)
                        student.inscription_date = timezone.now()
                        student.save()
                        
                        current_code.student = student
                        current_code.save()
                        
                        return redirect('student-detail', pk=student.pk)
                    else : 
                        return display_message(request, "Ce code d'inscription n'existe pas. (-> a déjà été utilisé ). ")
        else : # formulaire incorrect
            print (form.errors )
            return send_form_for_inscription(request, sent_code, "", form)

    elif request.method == "GET":
        sent_code = request.GET.get('lb-code', None)
        if sent_code is not None : 
            request.session['sent_code'] = sent_code
        message = "Bonjour, veuillez finaliser votre inscription avec le professeur"
        return send_form_for_inscription(request, request.session['sent_code'], message)

def send_form_for_inscription(request, sent_code, message="", form = StudentForm() ):
    if sent_code is None or sent_code=="": 
        return display_message(request,  "Le code d'inscription n'a pas été récupéré.")
    else :
        current_teatcher, current_student = get_teatcher_and_student_from_code( sent_code )
        if current_teatcher is None : 
            return display_message(request,  "Ce code d'inscription n'existe pas.")
        else:
            if current_student is not None :    
                return display_message(request,  "Ce code d'inscription n'existe pas. (-> a déjà été utilisé)")
            else :
                if message=="Bonjour, veuillez finaliser votre inscription avec le professeur" :
                        
                    message += f" {str(current_teatcher)}" 
                datas = {'sent_code' : sent_code, 'teatcher' : current_teatcher, 'form': form, 'message': message}
                return render(request, 'inscription_pedago/student_edit.html', datas)
        
def get_teatcher_and_student_from_code( str_code ) :
    current_code_s = Validation_code.objects.filter(code=str(str_code))
    if len( current_code_s )!= 1 :
        return None, None
    else:
        current_code = current_code_s[0]
        return current_code.teatcher, current_code.student
        

def get_teatcher_from_id_or_none( id_teatcher ):
    teatchers = Teatcher.objects.filter(pk=int(id_teatcher))
    if len(teatchers) !=1 : 
        return None
    else :                  
        return teatchers[0]  

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

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        if self.request.session['sent_code'] :
            url_prof = Validation_code.objects.filter(code=self.request.session['sent_code'])[0].teatcher.url_site

            context['url_prof'] = url_prof
        return context

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

    #.......... reprise du code avec les teatchers

class TeatcherDetail(DetailView):
    model = Teatcher

    # def get_queryset(self):
    #     return object.discipline_set.all()

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)

    #     context['disciplines'] = Discipline.objects.filter(developer = self.object)         
    #     return context


def instruments(request):
    return render(request, 'inscription_pedago/instruments.html', {} )

from .forms import ContactForm, ContactForm2
def contact(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ContactForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return redirect('will_contact')

        else:
            print('CONTACT FORM invalid')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ContactForm()

    return render(request, 'inscription_pedago/contact.html', {'form': form} )
    # return render(request, 'inscription_pedago/contact.html', {} )

from inscription_pedago.models import ContactModel

from django.urls import reverse_lazy
class ContactCreate(CreateView) :
    template_name = "inscription_pedago/contact.html"
    # model = ContactModel   
    form_class = ContactForm2
    # fields = fields = ['name', 'phone_number', 'demandes_particulieres']
    success_url = reverse_lazy('test_learnbox:wewillcontactyou') #"will_contact"

def will_contact(request):
    return render(request, 'inscription_pedago/wewillcontactyou.html', {'message': 'Votre demande a bien été prise en compte, nous vous rappellerons sous 48 heures.'} )
 

from django.core.mail import send_mail

def test_mail(request):
    print( 'test_mail->')
    send_mail(
        'Subject here',
        'Here is the message.',
        'softs.musics@gmail.com',
        ['to@example.com'],
        fail_silently=False,
    )
    return HttpResponse( 'test mail done.' )