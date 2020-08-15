from .models import Student

# 导入序列化模块
from rest_framework import serializers

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('stu_name', 'stu_age', 'stu_email')


