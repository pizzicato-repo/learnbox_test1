from django.db import models
from django.urls import reverse

class Student(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    email = models.EmailField()
    date_of_birth = models.DateTimeField('date of birth')
    inscription_date = models.DateTimeField('date of inscription')

    def get_absolute_url(self):
        return reverse('student-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.surname +' '+ self.name +' ('+ self.email +')'

class Discipline(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Teatcher(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    url_site = models.CharField(max_length=200, default='url_vide')

    disciplines = models.ManyToManyField(Discipline)

    def __str__(self):
        return self.surname +' '+ self.name