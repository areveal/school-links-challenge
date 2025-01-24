from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from exams.factories import ResultPropertyFactory
from exams.models import ResultProperty


class ResultPropertySerializer(serializers.ModelSerializer):
    value = serializers.JSONField(write_only=True)

    class Meta:
        model = ResultProperty
        fields = ["id", "result", "attribute", "value"]
        read_only_fields = ["result"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.result = self.context.get("result")
        if self.result:
            # Limit available attributes for selection to ExamAttributes related to the given Result
            self.fields["attribute"].queryset = self.result.exam.attributes

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["value"] = instance.value

        return representation

    def validate(self, data):
        """
        Ensure value being passed matches data type of given attribute
        """
        exam_definition = data["attribute"]
        value = data["value"]

        # Match the value against the data type of the exam definition
        expected_type = exam_definition.data_type
        if not isinstance(value, eval(expected_type)):
            raise ValidationError({"value": f"Must be of type {expected_type}"})

        return data

    def create(self, validated_data):
        """
        Create ResultProperty using ResultProperty factory to handle data types
        """
        attribute = validated_data.get("attribute")
        factory = ResultPropertyFactory(attribute.data_type)

        return factory.make(
            result=self.result,
            attribute=attribute,
            value=validated_data.get("value")
        )

