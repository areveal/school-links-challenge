from rest_framework import serializers

from exams.models import ExamAttribute


class ExamAttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamAttribute
        fields = "__all__"
