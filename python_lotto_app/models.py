from django.db import models

# Create your models here.

# Lotto Infomation
class lottoBoard(models.Model):
    round = models.IntegerField(primary_key=True)
    number_1 = models.CharField(max_length=20, blank=False)
    number_2 = models.CharField(max_length=20, blank=False)
    number_3 = models.CharField(max_length=20, blank=False)
    number_4 = models.CharField(max_length=20, blank=False)
    number_5 = models.CharField(max_length=20, blank=False)
    number_6 = models.CharField(max_length=20, blank=False)
    number_7 = models.CharField(max_length=20, blank=False)
    date = models.DateField(null=True)