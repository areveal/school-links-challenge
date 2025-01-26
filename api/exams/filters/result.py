from django_filters import rest_framework
from django_filters.rest_framework import FilterSet

from exams.models import Result


class ResultFilterSet(FilterSet):
    exam_name = rest_framework.CharFilter(field_name="exam__name", lookup_expr="iexact")
    subject = rest_framework.CharFilter(field_name="exam__subject", lookup_expr="iexact")
    grade = rest_framework.CharFilter(field_name="exam__grade", lookup_expr="iexact")
    state = rest_framework.CharFilter(field_name="exam__state", lookup_expr="iexact")

    class Meta:
        model = Result
        fields = []
