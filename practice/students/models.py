from django.db import models

class Student(models.Model):
    Full_name = models.TextField()
    Date_of_birth = models.DateField(null=True)
    Course = models.IntegerField()
    Specialty = models.TextField()
    Number_phone = models.TextField()
    Faculty = models.TextField()
    Gender = models.TextField()
    Group = models.TextField()

    def __str__(self):
        return self.Full_name

class Faculty(models.Model):
    Title = models.CharField(max_length=100)
    Headmaster = models.TextField()
    Cabinet = models.TextField()
    Number_phone = models.TextField()

    def __str__(self):
        return self.Title

class Group(models.Model):
    Number = models.TextField()
    Headman = models.TextField()
    Specialty = models.TextField()
    Faculty = models.TextField()

    def __str__(self):
        return self.Number

class Specialty(models.Model):
    Title = models.TextField()

    def __str__(self):
        return self.Title

class Department(models.Model):
    Title = models.CharField(max_length=100)
    Headmaster = models.TextField()

    def __str__(self):
        return self.Title

class Teacher(models.Model):
    Full_name = models.TextField()
    Age = models.IntegerField()
    Specialty = models.TextField()
    Number_phone = models.TextField()
    Faculty = models.TextField()
    Gender = models.TextField()

    def __str__(self):
        return self.Full_name