from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Course, Assessment
from .serializers import CourseSerializer, AssessmentSerializer

class CourseAPIView(APIView):

    def get(self, request):
        course = Course.objects.all()
        serializer = CourseSerializer(course, many=True)
        return Response(serializer.data)

class AssessmentAPIView(APIView):
    
    def get(self, request):
        assessment = Assessment.objects.all()
        serializer = AssessmentSerializer(assessment, many=True)
        return Response(serializer.data)