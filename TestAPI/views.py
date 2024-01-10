from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import  status
from .models import Course
from .serializers import GetAllCourseSerializers, CoursePostAPISerializers
# Create your views here.


class GetAllCourseAPI(APIView):
    def get(self, request):
        list_course = Course.objects.all()
        my_data = GetAllCourseSerializers(list_course, many=True)
        return Response(data=my_data.data, status=status.HTTP_200_OK)

    def post(self, request):
        my_data = CoursePostAPISerializers(data=request.data)
        if not my_data.is_valid():
            return Response("woring information", status=status.HTTP_400_BAD_REQUEST)
        cs = Course.objects.create(title= my_data.data['title1'],
                              content= my_data.data['content1'], price= my_data.data['price1'])

        return Response(data=cs.id, status=status.HTTP_200_OK)

