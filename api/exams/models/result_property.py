from django.db import models
from polymorphic.models import PolymorphicModel


class ResultProperty(PolymorphicModel):
    """Model to represent non-standard properties of a given exam result, i.e. 'exam_code', 'exam_subject', etc."""
    class Meta:
        abstract = False

    attribute = models.ForeignKey('exams.ExamAttribute', related_name="values", on_delete=models.CASCADE)
    result = models.ForeignKey('exams.Result', related_name="properties", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.attribute.name}: {self.value}"


class StringResultProperty(ResultProperty):
    value = models.CharField(max_length=100)


class IntegerResultProperty(ResultProperty):
    value = models.IntegerField()


class FloatResultProperty(ResultProperty):
    value = models.FloatField()


class BooleanResultProperty(ResultProperty):
    value = models.BooleanField()


class DateResultProperty(ResultProperty):
    value = models.DateField()


class DateTimeResultProperty(ResultProperty):
    value = models.DateTimeField()
