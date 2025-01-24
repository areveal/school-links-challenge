from rest_framework import serializers

from exams.models import ResultProperty


class ResultPropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = ResultProperty
        fields = "__all__"
