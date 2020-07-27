from django.contrib.auth.models import User, Group
from restapp.models import ClassStudent
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class ClassSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ClassStudent
        fields = ['student_name', 'rollno']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']