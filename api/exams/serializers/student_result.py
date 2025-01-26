from rest_framework import serializers

from exams.models import Result


class StudentResultSerializer(serializers.ModelSerializer):
    exam_name = serializers.CharField(source="exam.name")
    state = serializers.CharField(source="exam.state")
    subject = serializers.CharField(source="exam.subject")
    grade = serializers.CharField(source="exam.grade")

    class Meta:
        model = Result
        fields = ["exam_name", "state", "subject", "grade", "score"]
