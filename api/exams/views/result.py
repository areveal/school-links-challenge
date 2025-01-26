from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework import filters
from django_filters import rest_framework

from exams.filters import ResultFilterSet
from exams.models import Result
from exams.serializers import ResultSerializer


class ResultsListCreateView(generics.ListCreateAPIView):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer
    permission_classes = [AllowAny]
    filter_backends = [filters.OrderingFilter, rest_framework.DjangoFilterBackend, filters.SearchFilter]
    filterset_class = ResultFilterSet
    search_fields = ['student__first_name', 'student__last_name']
    ordering_fields = ['score', 'date']
    ordering = ['-date']


class ResultDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer
    permission_classes = [AllowAny]
