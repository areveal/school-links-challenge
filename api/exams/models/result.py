from django.db import models


class Result(models.Model):
    """A model representation of an Exam Result by a given Student"""
    student = models.ForeignKey('students.Student', related_name="results", on_delete=models.CASCADE)
    exam = models.ForeignKey('exams.Exam', related_name='results', on_delete=models.CASCADE)
    date = models.DateTimeField()  # Indicates the date that the test was submitted/taken

    def __str__(self):
        return f"{self.exam.code} result for {self.student}"
