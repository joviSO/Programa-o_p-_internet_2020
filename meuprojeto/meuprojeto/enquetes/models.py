from django.db import models

class Enquete(object):
    def __init__(self, texto = '', data = '', id = 0):
        self.texto = texto
        self.data = data
        self.id = id
# Create your models here.
