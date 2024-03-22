from django.db import models

class Brand(models.Model):
    brand_name = models.CharField('Nome da marca', max_length=200)
    foundation_Date  = models.DateTimeField('Data de Fundação')

    def __str__(self):
        return self.brand_name

    def was_published_recently(self):
        return self.foundation_Date >= timezone.now() - datetime.timedelta(days=1)


class Car(models.Model):
    brand = models.ForeignKey( Brand, on_delete=models.CASCADE)
    car_name = models.CharField('Nome do carro', max_length=200)
    value_car = models.IntegerField('Valor do carro', default=0)

    def __str__(self):
        return self.car_name