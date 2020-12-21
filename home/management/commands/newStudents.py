from django.core.management.base import BaseCommand
from faker import Faker # noqa
from home.models import Student # noqa


class Command(BaseCommand):

    help = 'Add new student(s), default count of new students = 10' # noqa

    def add_arguments(self, parser):
        parser.add_argument('-c', '--count', type=int, default=10)

    def handle(self, *args, **options):
        faker = Faker()
        self.stdout.write('Insert new students.')
        for _ in range(options['count']):
            student = Student()
            student.name = faker.first_name()
            student.surname = faker.last_name()
            student.age = faker.random_int(min=0, max=150)
            student.sex = faker.simple_profile()['sex']
            student.address = faker.address()
            student.description = faker.text()
            student.birthday = faker.date_of_birth()
            student.email = faker.email()
            student.save()
        self.stdout.write('End inserting new students.')
