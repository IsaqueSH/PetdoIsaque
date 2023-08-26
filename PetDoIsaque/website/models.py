from django.db import models

class Produto(models.Model):
    criado_em = models.DateTimeField(auto_now_add = True)
    nome_produto = models.CharField(max_length = 100)
    marca_produto = models.CharField(max_length = 50)
    pet_produto = models.CharField(max_length = 100)
    tipo_produto = models.CharField(max_length = 100)
    preco_produto = models.FloatField()
    apresentacao_produto = models.CharField(max_length = 100)
    
