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

class Teatcher(models.Model):
    name = models.CharField(max_length=200)

