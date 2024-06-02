from django.urls import path
from .views import CourseAPIView, AssessmentAPIView

urlpatterns = [
    path('courses/', CourseAPIView.as_view(), name='courses'),
    path('courses/<int:pk>/', CourseAPIView.as_view(), name='course-detail'),
    path('assessments/', AssessmentAPIView.as_view(), name='assessments'),
    path('assessments/<int:pk>/', AssessmentAPIView.as_view(), name='assessment-detail'),
]
