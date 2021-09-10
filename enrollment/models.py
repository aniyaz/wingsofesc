from django.db import models
from django.db.models.base import Model

# Create your models here.
class Enrollment(models.Model):
    uid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    gender = models.CharField(max_length=6)
    father_name = models.CharField(max_length=50)
    birth_year = models.IntegerField()
    primary_phone = models.CharField(max_length=13)
    is_whatsapp = models.BooleanField()
    whatsapp_number = models.CharField(max_length=13)
    hs_year = models.IntegerField()
    enroll_year = models.IntegerField()
    stream = models.IntegerField()
    current_profession = models.CharField(max_length=50)
    reserved_string = models.CharField(max_length=50)