import datetime
from unittest import TestCase

from ddt import ddt, unpack, data
from django.utils import timezone

from exams.models import (
    Result,
    StringResultProperty,
    IntegerResultProperty,
    FloatResultProperty, BooleanResultProperty, DateResultProperty, DateTimeResultProperty
)
from exams.serializers import ResultPropertySerializer
from exams.tests.factories import ExamAttributeFactory, ResultFactory


@ddt
class TestResultPropertySerializer(TestCase):
    def setUp(self):
        self.result = ResultFactory.create()
        self.exam_attribute = ExamAttributeFactory.create()

    @unpack
    @data(
        ["str", "hello world", StringResultProperty],
        ["int", 4, IntegerResultProperty],
        ["float", 3.14, FloatResultProperty],
        ["bool", True, BooleanResultProperty],
        ["date", timezone.now().date(), DateResultProperty],
        ["datetime", timezone.now(), DateTimeResultProperty],
    )
    def test_create(self, data_type, value, result_property_model):
        self.exam_attribute.data_type = data_type
        validated_data = {
            "attribute": self.exam_attribute,
            "value": value
        }
        serializer = ResultPropertySerializer()
        serializer.result = self.result
        result_property = serializer.create(validated_data)

        self.assertTrue(isinstance(result_property, result_property_model))
        self.assertEqual(result_property.value, value)
        self.assertEqual(result_property.attribute, self.exam_attribute)
        self.assertEqual(result_property.result, self.result)