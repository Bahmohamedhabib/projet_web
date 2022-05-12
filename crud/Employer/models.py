
from django.db import models


class Position(models.Model):
    title=models.CharField(max_length=100)
    
    def __str__(self):
        return self.title

class Employer_enregister(models.Model):
    nom=models.CharField(max_length=255)
    emp_code=models.CharField(max_length=6)
    mobile=models.CharField(max_length=20)
    position=models.ForeignKey(Position,on_delete=models.CASCADE)
    

# Create your models here.
