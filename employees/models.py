from django.db import models
from phone_field import PhoneField


class Position(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Employee(models.Model):
    surname = models.CharField(max_length=128)
    name = models.CharField(max_length=128)
    patronymic = models.CharField(max_length=128)
    birthday = models.DateField()
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    phone = PhoneField()