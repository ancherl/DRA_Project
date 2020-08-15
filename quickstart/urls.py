from django.urls import path, include

# 配置restapi的路由
from rest_framework import routers

from .views import StudentView

# 实例化router
router = routers.SimpleRouter()
# 注册StudentViewSet, 然后自动生成URL
router.register('student', StudentView)

urlpatterns = [
    path('v1/', include(router.urls))
]