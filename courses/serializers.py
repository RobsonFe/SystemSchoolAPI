from rest_framework import serializers
from .models import Course, Assessment

class AssessmentSerializer(serializers.ModelSerializer):
    class Meta:
        extra_kwargs = {
            'email': {'write_only': True}
        }
        model = Assessment
        fields = (
            'id',
            'course',
            'name',
            'email',
            'comment',
            'create',
            'active'
        )

class CourseSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Course
        fields = (
            'id',
            'title',
            'url',
            'create',
            'active'
        )