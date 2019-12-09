from django import forms

from .models import Student, ContactModel

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('name', 'surname', 'email', 'date_of_birth' ) #'date_of_birth',

# Les deux codes sont presque équivalents
class ContactForm(forms.Form):
    name = forms.CharField(label='Nom de votre entreprise *', max_length=100,   widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone_number = forms.RegexField(regex=r'^[0+][\d]+$',label=" Numéro de téléphone *",
                                    min_length=10, max_length=13, 
                                    error_messages={'invalid': 'Numéro de téléphone invalide'}, 
                                    widget=forms.TextInput(attrs={'class': 'form-control'}))
    demandes_particulieres = forms.CharField(label=' Demande particlulières', widget=forms.Textarea)

class ContactForm2(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields = ('name', 'phone_number', 'demandes_particulieres')
        # fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'demandes_particulieres': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'name': "Nom de la société",
            'phone_number': "Numéro de téléphone",
            'demandes_particulieres': "demandes particulieres",
            }

    # def save(self, commit=True):
    #     user.set_password(self.cleaned_data["password1"])
    #     if commit:
    #         user.save()
    #     return user