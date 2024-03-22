from django.db import models

# Create your models here.
class Marca(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.nome

class Categoria(models.Model):
    nome = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.nome

class Produto(models.Model):
    descricao = models.CharField(max_length=50)
    preco = models.FloatField()
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    categoria = models.ManyToManyField(Categoria)

    def __str__(self) -> str:
        return self.descricao