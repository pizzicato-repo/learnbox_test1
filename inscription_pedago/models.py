from django.db import models
from django.urls import reverse

class Student(models.Model):
    student_name = models.CharField(max_length=200)
    inscription_date = models.DateTimeField('date of inscription')

    def get_absolute_url(self):
        return reverse('student-detail', kwargs={'pk': self.pk})

class Teatcher(models.Model):
    teatcher_name = models.CharField(max_length=200)

