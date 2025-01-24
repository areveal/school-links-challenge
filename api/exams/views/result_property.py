from rest_framework import generics
from rest_framework.permissions import AllowAny

from exams.models import ResultProperty
from exams.serializers import ResultPropertySerializer


class ResultPropertyListCreateView(generics.ListCreateAPIView):
    queryset = ResultProperty.objects.all()
    serializer_class = ResultPropertySerializer
    permission_classes = [AllowAny]


class ResultPropertyDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ResultProperty.objects.all()
    serializer_class = ResultPropertySerializer
    permission_classes = [AllowAny]
