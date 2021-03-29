from home.models import Book, Student, Subject, Teacher  # noqa
from rest_framework import serializers  # noqa I003


class BookSerializer(serializers.ModelSerializer):

    class Meta:

        model = Book
        fields = ['title', 'created_at', 'update_at']


class StudentSerializer(serializers.ModelSerializer):

    book = BookSerializer(many=False, read_only=True)

    class Meta:

        model = Student
        fields = ['name', 'surname', 'age', 'sex', 'address',
                  'description', 'birthday', 'email', 'book', 'created_at', 'update_at']


class SubjectSerializer(serializers.ModelSerializer):

    class Meta:

        model = Subject
        fields = ['name_of_subject', 'created_at', 'update_at']


class TeacherSerializer(serializers.ModelSerializer):

    class Meta:

        model = Teacher
        fields = ['name', 'surname', 'created_at', 'update_at']
