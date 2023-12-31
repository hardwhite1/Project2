from django.db import models

# Create your models here.
class Member(models.Model):
    firstname = models.CharField(max_length=155)
    lastname = models.CharField(max_length=155)
    phone = models.IntegerField(null=True)
    joined_date = models.DateField(null=True)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"