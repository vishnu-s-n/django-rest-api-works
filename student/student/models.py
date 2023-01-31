from django.db import models

# Create your models here.
from student.utils import genderEnumType,GradeEnumType,SemEnumType,BranchEnumType


class studentSModel(models.Model):
    name=models.CharField(max_length=150)
    date_of_birth=models.DateField()
    gender = models.CharField(max_length=120, choices=genderEnumType.choices())
    image=models.ImageField(upload_to="image",null=True)

    def __str__(self):
        return self.name



class studentMarkModel(models.Model):
    owner=models.ForeignKey(studentSModel,on_delete=models.CASCADE,related_name="StudentMarkModel_owner")

    grade = models.CharField(max_length=120, choices=GradeEnumType.choices())

    sem = models.CharField(max_length=150,choices=SemEnumType.choices())

    def __str__(self):
        return self.grade




class studentMainModel(models.Model):
    owner= models.OneToOneField(studentSModel,on_delete=models.CASCADE)
    marks=models.ManyToManyField(studentMarkModel)
    branch = models.CharField(max_length=150, choices=BranchEnumType.choices())

    def __str__(self):
        return self.branch


