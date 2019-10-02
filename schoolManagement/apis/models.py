from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class School(models.Model):
	Name = models.CharField(max_length=100)
	Admin = models.OneToOneField(User,on_delete=models.CASCADE,related_name='school-admin')

class Student(models.Model):
	student = models.OneToOneField(User,on_delete=models.CASCADE,related_name='student')
	name = models.CharField(max_length=100)
	age = models.IntegerField()
	school = models.ForeignKey(School)

	@property
	def is_adult(self):
		return (if self.age > 18)

