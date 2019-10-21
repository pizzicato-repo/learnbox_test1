from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=200)
    inscription_date = models.DateTimeField('date of inscription')


class Teatcher(models.Model):
    name = models.CharField(max_length=200)

