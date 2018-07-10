from django.db import models
import uuid

class Arquivo(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    descricao = models.CharField(max_length = 255, blank = False)
    data = models.DateField(auto_now_add = True)
    copias = models.IntegerField(blank = False, null = False)
    nome = models.CharField(max_length = 70, blank = False)

    def __str__(self):
        return self.nome

class Usuario(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    nome = models.CharField(max_length = 255, blank = False)
    matricula = models.IntegerField(blank=False, null = False, unique = True)
    email = models.EmailField(max_length = 70, blank = False, null = False, unique = True )
    check = models.BooleanField()

    def __str__(self):
        return self.nome

