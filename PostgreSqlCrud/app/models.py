from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=100)


class Teacher(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField()
    dept = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)
    

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField()
    class_teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, blank=True)
    


    
