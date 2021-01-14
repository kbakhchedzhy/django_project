from django.db import models


class Student(models.Model):

    id = models.AutoField(primary_key=True) # noqa
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    age = models.IntegerField()
    sex = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    description = models.TextField()
    birthday = models.DateField()
    email = models.CharField(max_length=200)
    social_url = models.CharField(max_length=500, null=True, blank=True)
    is_active = models.CharField(max_length=500, null=True, blank=True)
    normalized_name = models.CharField(max_length=500, null=True, blank=True)

    subject = models.ForeignKey('home.Subject',
                                on_delete=models.SET_NULL,
                                null=True)
    book = models.OneToOneField('home.Book',
                                on_delete=models.CASCADE,
                                null=True)


class Subject(models.Model):

    # one to many
    id = models.AutoField(primary_key=True) # noqa
    name_of_subject = models.CharField(max_length=200)


class Book(models.Model):

    # one to one
    id = models.AutoField(primary_key=True) # noqa
    title = models.CharField(max_length=200)


class Teacher(models.Model):

    # one to many
    id = models.AutoField(primary_key=True) # noqa
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)

    student = models.ManyToManyField('home.Student')
