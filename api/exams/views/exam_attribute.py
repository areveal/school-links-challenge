from rest_framework import generics
from rest_framework.permissions import AllowAny

from exams.models import ExamAttribute
from exams.serializers import ExamAttributeSerializer


class ExamAttributeListCreateView(generics.ListCreateAPIView):
    queryset = ExamAttribute.objects.all()
    serializer_class = ExamAttributeSerializer
    permission_classes = [AllowAny]


class ExamAttributeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ExamAttribute.objects.all()
    serializer_class = ExamAttributeSerializer
    permission_classes = [AllowAny]
