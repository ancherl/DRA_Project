from django.shortcuts import render

from rest_framework import viewsets

# 把自定义的序列化器拿过来
from .serializers import StudentSerializer

# 把模型拿过来
from .models import Student

# Create your views here.

class StudentView(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()


