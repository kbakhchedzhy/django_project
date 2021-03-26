from unittest import skip

from django.test import TestCase # noqa
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from home.models import Student, Book


class StudentApiTests(APITestCase):

    def setUp(self) -> None:
        Student.objects.create(name='Zero',
                               surname='Admin',
                               book=Book.objects.create(title='idx3242342'))

    def test_get_students(self):
        response = self.client.get(reverse('students_api-list'))
        result = {'count': 1,
                  'next': None,
                  'previous': None,
                  'results': [{'address': None,
                               'age': None,
                               'birthday': None,
                               'book': {'title': 'idx3242342'},
                               'description': None,
                               'email': None,
                               'name': 'Zero',
                               'sex': 'unknown',
                               'surname': 'Admin'}]
                  }
        self.assertEqual(response.json(),
                         result
                         )

    def test_create_students(self):
        data = {
            "name": "string",
            "surname": "string",
            "book": {'title': '6745rtfh'}
            }
        response = self.client.post(reverse('students_api-list'),
                                    data=data, format='json'
                                    )
        self.assertEqual(response.status_code,
                         status.HTTP_201_CREATED)
        students = Student.objects.all()
        self.assertEqual(students.count(), 2)

    def test_update_students(self):
        students = Student.objects.all()
        data = {
            'name': 'Second',
            'surname': 'User2',
            'age': 20,
            }
        response = self.client.put(reverse('students_api-detail',
                                           kwargs={'pk': students[0].id}),
                                   data=data, format='json'
                                   )
        result = {'address': None,
                   'age': 20,
                   'birthday': None,
                   'book':  {'title': 'idx3242342'},
                   'description': None,
                   'email': None,
                   'name': 'Second',
                   'sex': 'unknown',
                   'surname': 'User2'
                  }

        self.assertEqual(response.json(), result)

    def test_delete_students(self):
        students = Student.objects.all()
        self.client.delete(reverse('students_api-detail',
                                           kwargs={'pk': students[0].id}))
        students = Student.objects.all()
        self.assertEqual(students.count(), 0)




