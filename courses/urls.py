from django.urls import path
from .views import CourseAPIView, CoursesAPIView, AssessmentAPIView, AssessmentsAPIView

urlpatterns = [
    path('courses/', CoursesAPIView.as_view(), name='courses'),
    path('courses/<int:pk>', CourseAPIView.as_view(), name='courses'),
    path('assessments/', AssessmentsAPIView.as_view(), name='assessments'),
    path('assessments/<int:pk>', AssessmentAPIView.as_view(), name='assessments'),
]
