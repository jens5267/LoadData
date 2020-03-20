from django.db import models

# from django_mysql.models import ListCharField

# Create your models here.
class Load(models.Model):
    first_input = models.FloatField()
    second_input = models.FloatField()
