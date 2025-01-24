from django.db import models


class ExamAttribute(models.Model):
    class DataTypeChoices(models.TextChoices):
        STRING = "str", "String"
        INTEGER = "int", "Integer"
        FLOAT = "float", "Float"
        BOOLEAN = "bool", "Boolean"
        DATE = "date", "Date"
        DATETIME = "datetime", "Datetime"


    exam = models.ForeignKey('exams.Exam', related_name="attributes", on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    data_type = models.CharField(choices=DataTypeChoices.choices, default=DataTypeChoices.STRING, max_length=20)

    def __str__(self):
        return f"{self.name} ({self.data_type})"
