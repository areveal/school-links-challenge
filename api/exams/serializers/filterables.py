from rest_framework import serializers


class FilterablesSerializer(serializers.Serializer):
    exam_names = serializers.ListField(child=serializers.CharField())
    subjects = serializers.ListField(child=serializers.CharField())
    grades = serializers.ListField(child=serializers.CharField())
    states = serializers.ListField(child=serializers.CharField())
