from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length= 20)
    roll_no = models.IntegerField()
    dob = models.DateField()
    marks = models.IntegerField()
    address = models.TextField()
    
