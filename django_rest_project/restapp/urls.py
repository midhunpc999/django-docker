from restapp import views
from django.urls import path
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'class-students', views.ClassViewSet)

urlpatterns = router.urls
