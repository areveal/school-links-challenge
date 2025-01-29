from unittest import TestCase
from unittest.mock import Mock, patch

from ddt import ddt, data, unpack

from exams.factories import ResultPropertyFactory
from exams.models import (
    ExamAttribute,
    StringResultProperty,
    IntegerResultProperty,
    FloatResultProperty,
    BooleanResultProperty,
    DateResultProperty,
    DateTimeResultProperty
)


@ddt
class TestResultPropertyFactory(TestCase):
    """
    Unit Test Class to assert that the inner behaviours of our ResultPropertyFactory methods are working as expected
    """
    def setUp(self):
        self.exam_attribute = ExamAttribute()
        self.kwargs = {
            "attribute": self.exam_attribute,
            "key": "value",
            "arbitrary": "data"
        }

    @data("str", "int", "bool", "float", "date", "datetime")
    def test_make(self, data_type):
        """
        Assert the calls within the ResultPropertyFactory make method
        """
        # Mock setup to ensure all we are testing is exactly what is inside this method
        mock_property_model = Mock(name="ResultProperty model")
        self.expected_return = Mock(name="ResultProperty object")
        mock_property_model.objects.create = Mock(return_value=self.expected_return)
        ResultPropertyFactory.derive_result_property_model_class = Mock(return_value=mock_property_model)

        self.exam_attribute.data_type = data_type
        result = ResultPropertyFactory.make(**self.kwargs)
        ResultPropertyFactory.derive_result_property_model_class.assert_called_with(data_type=data_type)
        self.assertIs(result, self.expected_return)

    @data(
        ["str", StringResultProperty],
        ["int", IntegerResultProperty],
        ["float", FloatResultProperty],
        ["bool", BooleanResultProperty],
        ["date", DateResultProperty],
        ["datetime", DateTimeResultProperty],
    )
    @unpack
    def test_derive_result_property_model_class(self, data_type, result_property_model):
        """
        Assert the behaviour of the derive_result_property_model_class method
        """
        result = ResultPropertyFactory.derive_result_property_model_class(data_type)
        self.assertEqual(result, result_property_model)