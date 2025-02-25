from django.db import models

class Faculty(models.Model):
    Title = models.CharField(max_length=100)
    Headmaster = models.TextField()
    Cabinet = models.TextField()
    Number_phone = models.TextField()

    def __str__(self):
        return self.Title

class Specialty(models.Model):
    Title = models.TextField()
    Faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, default=1)
    Years = models.IntegerField(default=4)

    def __str__(self):
        return self.Title

class Group(models.Model):
    Number = models.TextField()
    Headman = models.TextField()
    Specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE, default=1)
    Faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.Number

class Student(models.Model):
    Full_name = models.TextField()
    Date_of_birth = models.DateField(null=True)
    Course = models.IntegerField()
    Specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE, default=1)
    Number_phone = models.TextField()
    Faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, default=1)
    Gender = models.TextField()
    Group = models.ForeignKey(Group, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.Full_name

class Department(models.Model):
    Title = models.CharField(max_length=100)
    Headmaster = models.TextField()

    def __str__(self):
        return self.Title

class Teacher(models.Model):
    Full_name = models.TextField()
    Age = models.IntegerField()
    Specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE, default=1)
    Number_phone = models.TextField()
    Faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, default=1)
    Gender = models.TextField()
    Subject = models.TextField(default=None)

    def __str__(self):
        return self.Full_name