from rest_framework import generics
from rest_framework.permissions import AllowAny

from exams import models
from exams import serializers


class ResultPropertyListCreateView(generics.ListCreateAPIView):
    """
    This class-based view provides functionality to list all ResultProperty
    of a specific Result object and to create new properties for it.
    """
    serializer_class = serializers.ResultPropertySerializer
    permission_classes = [AllowAny]

    def get_object(self):
        return models.Result.objects.get(id=self.kwargs.get("pk"))

    def get_queryset(self):
        """
        Returns: All ResultProperties for the given Result
        """
        return self.get_object().properties.all()

    def get_serializer_context(self):
        """
        The method extends the existing serializer context with additional details
        by including the result of the `get_object()` method.
        """
        context = super().get_serializer_context()
        context["result"] = self.get_object()
        return context


class ResultPropertyDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.ResultProperty.objects.all()
    serializer_class = serializers.ResultPropertySerializer
    permission_classes = [AllowAny]
