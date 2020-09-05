from django.db import models

class Enquete(models.Model):
    texto = models.CharField(max_length=150)
    data_publicacao = models.DateField()
# Create your models here.
