from django.db import models

# Create your models here.

class Student(models.Model):
    stu_name = models.CharField(max_length=50)
    stu_age = models.IntegerField()
    stu_email = models.CharField(max_length=200)

    def __str__(self):
        return '(stu_name=' + self.stu_name + ', stu_age=' + str(self.stu_age) + ', stu_email=' + self.stu_email + '  )'