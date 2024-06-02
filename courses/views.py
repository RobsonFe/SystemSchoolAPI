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

    def post(self, request):
        serializer = CourseSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    #   return Response({"msg": "Criado com sucesso"}, status=status.HTTP_201_CREATED)
    #   return Response({"id": serializer.data['id'], "curso": serializer.data['title']}, status=status.HTTP_201_CREATED)
        

class AssessmentAPIView(APIView):
    
    def get(self, request):
        assessment = Assessment.objects.all()
        serializer = AssessmentSerializer(assessment, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = AssessmentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)