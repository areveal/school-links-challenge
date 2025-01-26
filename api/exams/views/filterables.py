from rest_framework import views
from rest_framework.response import Response

from exams.models import Exam
from exams.serializers import FilterablesSerializer


class FilterablesRetrieveView(views.APIView):
    def get(self, request, *args, **kwargs):
        data = {
            "exam_names": Exam.objects.filter(name__isnull=False).values_list("name", flat=True).distinct(),
            "subjects": Exam.objects.filter(subject__isnull=False).values_list("subject", flat=True).distinct(),
            "grades": Exam.GradeLevelChoices.values,
            "states": Exam.StateChoices.values
        }

        serializer = FilterablesSerializer(data)
        return Response(serializer.data)
