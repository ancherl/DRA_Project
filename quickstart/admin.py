from django.contrib import admin

from .models import Student

# Register your models here.
# 将自己的model 注册到django 的后台管理页面

# admin.site.register(Student)

# 设置模型设置管理类， 方便在后台进行管理
class StudentAdminInfo(admin.ModelAdmin):
    list_display = ['stu_name', 'stu_age', 'stu_email']
    search_fields = ['stu_name', 'stu_email']
    list_per_page = 10

admin.site.register(Student, StudentAdminInfo)

