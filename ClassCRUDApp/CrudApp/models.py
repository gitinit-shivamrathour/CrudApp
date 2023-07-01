from django.db import models

class EmployeeModel(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    address = models.TextField()
    phone = models.IntegerField()

    def __str__(self):
        return self.name