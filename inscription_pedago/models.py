from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=200)
    birth_date = models.DateTimeField('date of birth')


class Teatcher(models.Model):
    name = models.CharField(max_length=200)
