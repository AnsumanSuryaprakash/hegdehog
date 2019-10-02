from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User
from apis.models import School, Student


class SchoolSerializer(serializers.ModelSerializer):
	class Meta:
		model = School
		fields = ('id','name')

class StudentSerializer(serializers.ModelSerializer):
	school = SchoolSerializer(read_only=True)
	class Meta:
		model = Student
		fields = ('name','age','school','is_adult')

class StudentUserSerializer(serializers.ModelSerializer):
	student = StudentSerializer(required=True)
	class Meta:
		model = User
		fields = ('username','password','student')
		extra_kwargs = {'password':{'write_only':True}}

	def create(self,validated_data):
		student_data = validated_data.pop('student')
		password = validated_data.pop('password')
		user = User(**validated_data)
		user.set_password(password)
		user.save()
		Student.objects.create(user=user,**student_data)
		return user
	
class SchoolUserSerializer(serializers.ModelSerializer):
	School = SchoolSerializer(required=True)
	class Meta:
		model = User
		fields = ('username','password','school')
		extra_kwargs = {'password':{'write_only':True}}

	def create(self,validated_data):
		school_data = validated_data.pop('school')
		password = validated_data.pop('password')
		user = User(**validated_data)
		user.set_password(password)
		user.save()
		School.objects.create(user=user,**school_data)
		return user