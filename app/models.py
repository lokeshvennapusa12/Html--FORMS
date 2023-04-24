from django.db import models

# Create your models here.

class Student(models.Model):
    sid=models.IntegerField(primary_key=True)
    sname=models.CharField(max_length=100)
    phone=models.IntegerField()
    percentage=models.IntegerField()
    remarks=models.CharField(max_length=4)

    def __str__(self) -> str:
        return str(self.sid)
    

class Course(models.Model):
    cid=models.IntegerField(primary_key=True )
    sid=models.ForeignKey(Student,on_delete=models.CASCADE)
    course=models.CharField(max_length=100)
    college=models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.course
    