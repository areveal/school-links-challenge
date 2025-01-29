from exams.models import (
    ExamAttribute,
    StringResultProperty,
    IntegerResultProperty,
    FloatResultProperty,
    BooleanResultProperty,
    DateResultProperty,
    DateTimeResultProperty,
    ResultProperty
)


class ResultPropertyFactory:
    @staticmethod
    def derive_result_property_model_class(data_type) -> type[ResultProperty]:
        """
        Derives the appropriate result property model class based on the data type.
        """
        return {
            "str": StringResultProperty,
            "int": IntegerResultProperty,
            "float": FloatResultProperty,
            "bool": BooleanResultProperty,
            "date": DateResultProperty,
            "datetime": DateTimeResultProperty,
        }.get(data_type)

    @staticmethod
    def make(**kwargs) -> ResultProperty:
        """
        Factory make method that derives correct ResultProperty inherited model from the given ExamAttribute
        and then calls create with provided kwargs
        """
        exam_attribute = kwargs.get("attribute")
        data_type = exam_attribute.data_type
        result_property_model = ResultPropertyFactory.derive_result_property_model_class(data_type=data_type)

        return result_property_model.objects.create(**kwargs)