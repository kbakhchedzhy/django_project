from home.models import Book, Student, Subject, Teacher  # noqa
from rest_framework import serializers  # noqa I003


class BookSerializer(serializers.ModelSerializer):

    class Meta:

        model = Book
        fields = ['title']


class StudentSerializer(serializers.ModelSerializer):

    book = BookSerializer(many=False)

    class Meta:

        model = Student
        fields = ['name', 'surname', 'age', 'sex', 'address',
                  'description', 'birthday', 'email', 'book']


class SubjectSerializer(serializers.ModelSerializer):

    class Meta:

        model = Subject
        fields = ['name_of_subject']


class TeacherSerializer(serializers.ModelSerializer):

    class Meta:

        model = Teacher
        fields = ['name', 'surname']
