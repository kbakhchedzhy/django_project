from rest_framework import serializers

from home.models import Student, Subject, Teacher, Book


class StudentSerializer(serializers.ModelSerializer):

    class Meta:

        model = Student
        fields = ['name', 'surname', 'age', 'sex', 'address', 'description', 'birthday', 'email']


class SubjectSerializer(serializers.ModelSerializer):

    class Meta:

        model = Subject
        fields = ['name_of_subject']


class TeacherSerializer(serializers.ModelSerializer):

    class Meta:

        model = Teacher
        fields = ['name', 'surname']


class BookSerializer(serializers.ModelSerializer):

    class Meta:

        model = Book
        fields = ['title']
