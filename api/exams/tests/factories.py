from django.utils import timezone

import random
import factory

from exams.models import (
    ExamAttribute,
    Exam,
    Result,
    ResultProperty
)
from students.tests.factories import StudentFactory


class ExamFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Exam

    state = random.choice(Exam.StateChoices.choices)
    grade = random.choice(Exam.GradeLevelChoices.choices)
    name = factory.Faker('word')
    code = factory.Faker('word')
    max_score = random.choice(range(1000))
    subject = factory.Faker('word')


class ExamAttributeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ExamAttribute

    exam = factory.SubFactory(ExamFactory)


class ResultFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Result

    student = factory.SubFactory(StudentFactory)
    exam = factory.SubFactory(ExamFactory)
    date = factory.Faker('date_time', tzinfo=timezone.get_current_timezone())
    # score for a result should be any random number < the exam max_score
    score = factory.LazyAttribute(lambda o: random.choice(range(o.exam.max_score)))

