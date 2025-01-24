from rest_framework import serializers

from exams.models import Result
from exams.serializers import ExamSerializer
from students.serializers import StudentSerializer


class ResultSerializer(serializers.ModelSerializer):
    properties = serializers.JSONField(read_only=True)

    class Meta:
        model = Result
        fields = ["id", "student", "exam", "score", "date", "properties"]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        # Build custom properties dict
        properties = {}
        for result_property in instance.properties.all():
            properties.update({result_property.attribute.name: result_property.value})
        representation["properties"] = properties
        # We want repr of student to be the serialized data, but the write should retain the FK expectation.
        representation["student"] = StudentSerializer(instance.student).data
        # We want repr of exam to be the serialized data, but the write should retain the FK expectation.
        representation["exam"] = ExamSerializer(instance.exam).data
        return representation
