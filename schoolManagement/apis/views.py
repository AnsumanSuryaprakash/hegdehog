from django.shortcuts import render
from rest_framework import viewsets

from apis.model import School, Student
from apis.serializers import StudentUserSerializer, SchoolUserSerializer
from rest_framework.permissions import AllowAny
from schoolManagement.permissions import IsLoggedInUserOrAdmin, IsAdminUser


class SchoolUserViewSet(viewsets.ModelViewSet):
queryset = School.objects.all()
serializer_class = SchoolUserSerializer
def get_permissions(self):
    permission_classes = []
    if self.action == 'create':
      permission_classes = [AllowAny]
    elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
      permission_classes = [IsLoggedInUserOrAdmin]
    elif self.action == 'list' or self.action == 'destroy':
      permission_classes = [IsAdminUser]
    return [permission() for permission in permission_classes]



class StudentUserViewSet(viewsets.ModelViewSet):
queryset = Student.objects.all()
serializer_class = StudentUserSerializer

  def get_permissions(self):
    permission_classes = []
    if self.action == 'create':
      permission_classes = [AllowAny]
    elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
      permission_classes = [IsLoggedInUserOrAdmin]
    elif self.action == 'list' or self.action == 'destroy':
      permission_classes = [IsAdminUser]
    return [permission() for permission in permission_classes]


 class Liststudents(generics.ListAPIView):
 	serializer_class = StudentUserSerializer

 	def get_queryset(self):
 		schoolid = self.kwargs['schoolid']
 		studentList = Student.objects.filter(school_id = schoolid)
 		name = self.request.query_params.get('name', None)
 		age = self.request.query_params.get('age', None)

 		if not name and not age:
 			return studentList.orderby('name')
 		elif name and not age:
 			return studentList.filter(name=name).orderby('name')
 		elif not name and age:
 			return studentList.filter(age=age).orderby('name')
 		elif name and age:
 			return studentList.filter(name=name,age=age).orderby('name')