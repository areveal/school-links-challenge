from django_filters import rest_framework
from django_filters.rest_framework import FilterSet
from students.models import Student

class StudentFilterSet(FilterSet):
    exam_name = rest_framework.CharFilter(field_name="results__exam__name", lookup_expr="iexact")
    subject = rest_framework.CharFilter(field_name="results__exam__subject", lookup_expr="iexact")
    grade = rest_framework.CharFilter(field_name="results__exam__grade", lookup_expr="iexact")
    state = rest_framework.CharFilter(field_name="results__exam__state", lookup_expr="iexact")

    class Meta:
        model = Student
        fields = []
