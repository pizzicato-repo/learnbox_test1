from django.db import models
from django.urls import reverse

# class Student(models.Model):
#     name = models.CharField(max_length=200)
#     surname = models.CharField(max_length=200)
#     email = models.EmailField()
#     date_of_birth = models.DateTimeField('date of birth')
#     inscription_date = models.DateTimeField('date of inscription')

#     def get_absolute_url(self):
#         return reverse('student-detail', kwargs={'pk': self.pk})

#     def __str__(self):
#         return self.surname +' '+ self.name +' ('+ self.email +')'
    
#     def full_name(self):
#         return self.surname +' '+ self.name

# class Discipline(models.Model):
#     name = models.CharField(max_length=100)

#     def __str__(self):
#         return self.name

# class Teatcher(models.Model):
#     name = models.CharField(max_length=200)
#     surname = models.CharField(max_length=200, default='')
#     url_site = models.URLField(max_length=200, default='www.urlvide.fr')

#     disciplines = models.ManyToManyField(Discipline)
    

#     def __str__(self):
#         return self.surname +' '+ self.name

#     def full_name(self):
#         return self.surname +' '+ self.name

# class Validation_code(models.Model):
#     code = models.CharField(max_length=12)
#     teatcher = models.ForeignKey(Teatcher, on_delete=models.CASCADE)
#     student = models.ForeignKey(Student, null=True, on_delete=models.CASCADE)

#     def __str__(self):
#         str_student = '' if self.student is None else '-> '+ self.student.full_name()
#         return self.code +' ('+ str(self.teatcher) +')'+ str_student

class ContactModel(models.Model):
    MRS = 'MRS'
    MR = 'MR'
    GENRE = [ (MRS, 'Madame'), (MR, 'Monsieur'),]
    genre = models.CharField(
        max_length=3,
        choices=GENRE,
        verbose_name="Civilité",
    )
    name = models.CharField(max_length=12, verbose_name="Nom")
    surname = models.CharField(max_length=12, verbose_name="Prénom")
    enterprise_name = models.CharField(max_length=12, verbose_name="Société")
    phone_number    = models.CharField(max_length=20, verbose_name="numéro téléphone")
    demandes_particulieres = models.CharField(max_length=2000, default='', null=True, blank=True, verbose_name="demandes particulières")


    def __str__(self):
        return self.name +'    (' + self.phone_number + ')'

    class Meta:
        verbose_name = "Contact société"
        verbose_name_plural = "Contacts sociétés"