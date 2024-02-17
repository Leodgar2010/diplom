from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    patronymic = models.CharField(max_length=100)
    phone = models.CharField(max_length=13)

    def __str__(self):
        return f'Client: {self.first_name}'

class Hypothesis (models.Model):
    hypothesis_type = models.CharField (max_length=100)

class Disposition (models.Model):
    disposition_type = models.CharField (max_length=100)

class Sanction (models.Model):
    sanction_type = models.CharField (max_length=100)

class Client(Person):
    client_account = models.DecimalField(max_digits=13, decimal_places=2)
    hypothesis = models.ManyToManyField (Hypothesis)

class Lawyer(Person):
    lawyer_accesibility = models.BooleanField(default=True)
    lawyer_photo = models.ImageField(upload_to='lawyer_photo/')
    disposition = models.ManyToManyField (Disposition)
    clients = models.ManyToManyField (Client)

class Case (models.Model):
    lawyer = models.ForeignKey (Lawyer, default='Rollo Tomassi', on_delete=models.SET_DEFAULT )
    client = models.ForeignKey (Client, default = 'Jhon Doe', on_delete=models.SET_DEFAULT )
    sanction = models.ForeignKey (Sanction, default= 'Do Nothing', on_delete=models.SET_DEFAULT)
