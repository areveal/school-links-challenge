from rest_framework import serializers

from exams.serializers.student_result import StudentResultSerializer
from students.models import Student


class StudentSerializer(serializers.ModelSerializer):
    results = StudentResultSerializer(many=True)

    class Meta:
        model = Student
        fields = ["id", "first_name", "last_name", "district", "results"]
