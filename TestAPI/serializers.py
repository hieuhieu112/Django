from rest_framework import serializers
from .models import Course


class GetAllCourseSerializers(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ("id", "title")


class CoursePostAPISerializers(serializers.Serializer):
    title1 = serializers.CharField(max_length=255)
    content1 = serializers.CharField(max_length=1000)
    price1 = serializers.IntegerField()