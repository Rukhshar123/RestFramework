from django.db import models

class Employee(models.Model):
    fullname = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.CharField(max_length=50)
    contact = models.CharField(max_length=12)
    salary = models.CharField(max_length=10)

    def __str__(self):
        return self.fullname
