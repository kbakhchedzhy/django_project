from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm

from home.models import Book, Student, Subject, Teacher


class BookForm(ModelForm):

    class Meta:

        model = Book

        fields = ['title']


class StudentForm(ModelForm):

    class Meta:

        model = Student

        fields = ['name',
                  'surname',
                  'age',
                  'sex',
                  'address',
                  'description',
                  'birthday',
                  'email',
                  'social_url'
                  ]


class SubjectForm(ModelForm):

    class Meta:

        model = Subject

        fields = ['name_of_subject']


class TeacherForm(ModelForm):

    class Meta:

        model = Teacher

        fields = ['name', 'surname']


class UserSignUpForm(UserCreationForm):

    class Meta:

        model = User

        fields = ("username",
                  "email",
                  "password1",
                  "password2")
