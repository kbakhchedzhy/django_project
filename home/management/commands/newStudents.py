import uuid

from django.core.management.base import BaseCommand

from home.models import Book, Student, Subject, Teacher


class Command(BaseCommand):


    help = 'Add new student(s), default count of new students = 10' # noqa

    def add_arguments(self, parser):
        parser.add_argument('-c', '--count', type=int, default=10)

    def handle(self, *args, **options):
        from faker import Faker
        faker = Faker()
        self.stdout.write('Insert new students.')

        for _ in range(options['count']):

            subject, _ = Subject.objects.get_or_create(name_of_subject='Python Intro')  # noqa
            subject.save()

            book_of_student = Book()
            book_of_student.title = uuid.uuid4()
            book_of_student.save()

            student = Student()
            student.name = faker.first_name()
            student.surname = faker.last_name()
            student.age = faker.random_int(min=0, max=150)
            student.sex = faker.simple_profile()['sex']
            student.address = faker.address()
            student.description = faker.text()
            student.birthday = faker.date_of_birth()
            student.email = faker.email()
            student.subject = subject
            student.book = book_of_student
            student.save()

            teacher, _ = Teacher.objects.get_or_create(name='Bill', surname='Gates') # noqa

            teacher.student.add(student)
            teacher.save()

        self.stdout.write('End inserting new students.')
