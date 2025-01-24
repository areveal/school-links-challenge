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
    def __init__(self, data_type: ExamAttribute.DataTypeChoices):
        self.data_type = data_type

    def derive_result_property_model_class(self) -> type[ResultProperty]:
        """
        Derives the appropriate result property model class based on the data type.

        Returns:
        type[ResultProperty]
            The model class corresponding to the specified data type.
        """
        return {
            "str": StringResultProperty,
            "int": IntegerResultProperty,
            "float": FloatResultProperty,
            "bool": BooleanResultProperty,
            "date": DateResultProperty,
            "datetime": DateTimeResultProperty,
        }.get(self.data_type)

    def make(self, **kwargs) -> ResultProperty:
        return self.derive_result_property_model_class().objects.create(**kwargs)