from datetime import date

from django.db import models


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    email = models.EmailField()
    phone = models.CharField(max_length=12)
    address = models.CharField(max_length=100)
    birthDate = models.DateField(default=date(2003,1, 1))

class Teacher(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    email = models.EmailField()
    phone = models.CharField(max_length=12)
    address = models.CharField(max_length=100)
    birthDate = models.DateField(default=date(2003,1, 1))

class Course(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='courses')
    students = models.ManyToManyField(Student, related_name='courses')

class Assignment(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='assignments')
    dueDate = models.DateField(default=date(2021,1, 1))
    students = models.ManyToManyField(Student, related_name='assignments')

class Grade(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE, related_name='grades')
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='grades')
    grade = models.IntegerField()




