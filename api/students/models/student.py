from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, null=True, default=None)
    district = models.ForeignKey('districts.District', related_name="students", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
