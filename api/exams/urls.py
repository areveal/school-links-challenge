"""
URL configuration for api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import (
    ExamListCreateView,
    ExamDetailView,
    ResultsListCreateView,
    ResultDetailView,
    ExamAttributeListCreateView,
    ExamAttributeDetailView,
    ResultPropertyListCreateView,
    ResultPropertyDetailView,
    FilterablesRetrieveView,
)

urlpatterns = [
    # Exams Paths
    path('exams/', ExamListCreateView.as_view(), name="exams"),
    path('exams/<int:pk>/', ExamDetailView.as_view(), name="exam_details"),
    # Exam Attribute Paths
    path('exam-attributes/', ExamAttributeListCreateView.as_view(), name="exam_attributes"),
    path('exam-attributes/<int:pk>/', ExamAttributeDetailView.as_view(), name="exam_attribute_details"),
    # Result Paths
    path('results/', ResultsListCreateView.as_view(), name="results"),
    path('results/<int:pk>/', ResultDetailView.as_view(), name="result_details"),
    # Result Property Paths
    path('results/<int:pk>/result-properties/', ResultPropertyListCreateView.as_view(), name="result_properties"),
    path('result-properties/<int:pk>/', ResultPropertyDetailView.as_view(), name="result_property_details"),
    # Filterables Path
    path('filterables/', FilterablesRetrieveView.as_view(), name="filterables"),

]
