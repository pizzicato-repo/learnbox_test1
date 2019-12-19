from django import forms

from .models import Student, ContactModel

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('name', 'surname', 'email', 'date_of_birth' ) #'date_of_birth',

# Les deux codes sont !!presque!! équivalents
# class ContactForm(forms.Form):
#     name = forms.CharField(label='Nom de votre entreprise *', max_length=100,   widget=forms.TextInput(attrs={'class': 'form-control'}))
#     phone_number = forms.RegexField(regex=r'^[0+][\d]+$',label=" Numéro de téléphone *",
#                                     min_length=10, max_length=13, 
#                                     error_messages={'invalid': 'Numéro de téléphone invalide'}, 
#                                     widget=forms.TextInput(attrs={'class': 'form-control'}))
#     demandes_particulieres = forms.CharField(label=' Demande partic lulières', widget=forms.Textarea)

class ContactForm2(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields = ('genre', 'name', 'surname', 'enterprise_name', 'phone_number', 'demandes_particulieres')
        # fields = '__all__'
        widgets = {
            'genre' : forms.Select(attrs={'class': 'custom-select'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'surname': forms.TextInput(attrs={'class': 'form-control'}),
            'enterprise_name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'demandes_particulieres': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Votre Message'})            
        }
        labels = {
            'name' : 'Nom',
            'prenom' : 'Prénom',
            'enterprise_name': "Nom de la société",
            'phone_number': "Numéro de téléphone",
            'demandes_particulieres': "Demandes particulières",
            }
    phone_number = forms.RegexField(regex=r'^[0+][\d]+$', label="Numéro de Téléphone",
                                    min_length=10, max_length=13, 
                                    error_messages={'invalid': 'Numéro  invalide'}, 
                                    widget=forms.TextInput(attrs={'class': 'form-control require-input'}))

    
    # def save(self, commit=True):
    #     user.set_password(self.cleaned_data["password1"])
    #     if commit:
    #         user.save()
    #     return user