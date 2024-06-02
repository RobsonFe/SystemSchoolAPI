from rest_framework.views import APIView
from rest_framework import response
from rest_framework import status
from .models import Course, Assessment
from .serializers import CourseSerializers, AssessmentSerializer

class CourseAPIView(APIView):

    def get(self, request):
        course = Course.objects.all()
        serializer = CourseSerializers(course, many=True)
        return response(serializer.data)

class AssessmentAPIView(APIView):
    
    def get(self, request):
        assessment = Assessment.objects.all()
        serializer = AssessmentSerializer(assessment, many=True)
        return response(serializer.data)