from django.core.management.base import BaseCommand

from home.models import Student


class Command(BaseCommand):

    help = 'Delete the first student.' # noqa

    def handle(self, *args, **options):

        first_student = Student.objects.first()
        first_student.delete()
