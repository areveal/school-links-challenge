import factory

from districts.tests.factories import DistrictFactory
from students.models import Student


class StudentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Student

    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    district = factory.SubFactory(DistrictFactory)
