from django.db.models import Max
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters
from rest_framework.permissions import AllowAny

from students.filters import StudentFilterSet
from students.models import Student
from students.serializers import StudentSerializer


class StudentListCreateView(generics.ListCreateAPIView):
    serializer_class = StudentSerializer
    permission_classes = [AllowAny]
    filter_backends = [filters.OrderingFilter, filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['first_name', 'last_name']
    filterset_class = StudentFilterSet
    ordering_fields = ['score']

    def get_queryset(self):
        queryset = Student.objects.all()
        queryset = queryset.annotate(score=Max('results__score')).prefetch_related('results__exam').distinct()
        return queryset


class StudentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [AllowAny]
