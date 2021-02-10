import csv

from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic.base import View

from home.forms import BookForm, StudentForm, SubjectForm, TeacherForm
from home.models import Book, Student, Subject, Teacher


class StudentListView(View):
    """
    Output list of students.
    """

    def get(self, request): # noqa

        students = Student.objects.all()

        students_list = StudentForm()

        return render(request, 'student_list.html',
                      context={
                          'students': students,
                          'form': students_list}
                      )

    def post(self, request): # noqa

        if request.POST.get('filter_by', '') == 'filter_by_teacher':

            students = Student.objects.filter(
                teacher__name=request.POST.get('text_form', '')
            )

            return render(request, 'student_list.html', context={
                          'students': students})

        elif request.POST.get('filter_by', '') == 'filter_by_subject':

            students = Student.objects.filter(
                subject__name_of_subject=request.POST.get('text_form', '')
            )

            return render(request, 'student_list.html', context={
                          'students': students})

        elif request.POST.get('filter_by', '') == 'filter_by_book':

            students = Student.objects.filter(
                book__id=request.POST.get('text_form', '')
            )

            return render(request, 'student_list.html', context={
                          'students': students})

        return redirect(reverse('home'))


class StudentAddView(View):
    """
    Output forms for insert new students.
    """

    def get(self, request): # noqa
        students_form = StudentForm()
        book_form = BookForm()

        return render(request, 'student_add.html',
                      context={
                          'form': students_form,
                          'form_book': book_form}
                      )

    def post(self, request): # noqa
        book_form = BookForm(request.POST)
        book_form.save()
        student_form = StudentForm(request.POST)
        student_form.save()

        book = Book.objects.last()
        student = Student.objects.last()
        student.book = book
        student.save()
        return redirect(reverse('home'))


class StudentUpdateView(View):
    """
    Outputs fields with information about this student. Can update info.
    """

    def get(self, request, id): # noqa
        student = Student.objects.get(id=id)
        book = Book.objects.get(id=student.book_id)
        student_form = StudentForm(instance=student)
        form_book = BookForm(instance=book)
        context = {'form': student_form,
                   'form_book': form_book,
                   'student_id': student.id}
        return render(request, 'student_update.html', context=context)

    def post(self, request, id): # noqa
        student = Student.objects.get(id=id)
        student_form = StudentForm(request.POST, instance=student)
        if student_form.is_valid():
            student_form.save()
        return redirect(reverse('home'))


class BookListView(View):
    """
    Output list of books.
    """

    def get(self, request): # noqa

        books = Book.objects.all()

        return render(request, 'book_list.html',
                      context={
                          'books': books}
                      )


class BookInfoView(View):
    """
    Outputs fields with information about this book of
    every student. Can redirect on page for deleting book.
    """

    def get(self, request, id): # noqa
        book = Book.objects.get(id=id)
        context = {'book': book,
                   'book_id': book.id}
        return render(request, 'book_info.html', context=context)

    def post(self, request, id): # noqa
        book = Book.objects.get(id=id)
        book.delete()
        return redirect(reverse('books_list'))


class SubjectListView(View):
    """
    Output list of subjects.
    """

    def get(self, request): # noqa

        subjects = Subject.objects.all()

        return render(request, 'subject_list.html', context={
                    'subjects': subjects})


class SubjectInfoView(View):
    """
    Outputs fields with information about this subject and its student.
    """

    def get(self, request, id): # noqa
        subject = Subject.objects.get(id=id)
        subject_form = SubjectForm(instance=subject)
        this_subject_student = Student.objects.filter(subject=subject.id)
        new_students = Student.objects.exclude(subject=subject.id)
        context = {'form_subject': subject_form,
                   'subject_id': subject.id,
                   'subject': subject,
                   'this_subject_student': this_subject_student,
                   'new_students': new_students}
        return render(request, 'subject_info.html', context=context)

    def post(self, request, id): # noqa
        if 'change' in request.POST:
            subject = SubjectForm(request.POST)
            pre_save_subject = subject.save(commit=False)
            pre_save_subject.id = id
            pre_save_subject.save()

        elif 'delete' in request.POST:
            student = Student.objects.get(id=request.POST.get('delete', ''))
            subject = student.subject
            subject.student_set.remove(student)

        elif 'add' in request.POST:
            subject = Subject.objects.get(id=id)
            student = Student.objects.get(id=request.POST.get('add', ''))
            student.subject = subject
            student.save()

        return redirect(reverse('subjects_list'))


class TeacherListView(View):
    """
    Output list of subjects.
    """

    def get(self, request): # noqa

        teachers = Teacher.objects.all()

        return render(request, 'teacher_list.html', context={
                    'teachers': teachers}
                  )


class TeacherInfoView(View):
    """
    Outputs fields with information about this subject and its student.
    """

    def get(self, request, id): # noqa
        teacher = Teacher.objects.get(id=id)
        teacher_form = TeacherForm(instance=teacher)
        this_teacher_student = Student.objects.filter(teacher=teacher.id)
        new_students = Student.objects.exclude(teacher=teacher.id)
        context = {'form_teacher': teacher_form,
                   'teacher_id': teacher.id,
                   'teacher': teacher,
                   'this_teacher_student': this_teacher_student,
                   'new_students': new_students}
        return render(request, 'teacher_info.html', context=context)

    def post(self, request, id): # noqa
        if 'change' in request.POST:
            teacher = TeacherForm(request.POST)
            pre_save_teacher = teacher.save(commit=False)
            pre_save_teacher.id = id
            pre_save_teacher.save()

        elif 'delete' in request.POST:
            student = Student.objects.get(id=request.POST.get('delete', ''))
            teacher = Teacher.objects.get(student=student)
            teacher.student.remove(student)

        elif 'add' in request.POST:
            teacher = Teacher.objects.get(id=id)
            student = Student.objects.get(id=request.POST.get('add', ''))
            teacher.student.add(student)
            teacher.save()

        return redirect(reverse('teacher_info', kwargs={"id": teacher.id}))


class TeacherAddView(View):
    """
    Output forms for insert new teacher.
    """

    def get(self, request): # noqa
        teacher_form = TeacherForm()
        new_students = Student.objects.all()

        return render(request, 'teacher_add.html',
                      context={
                          'form': teacher_form,
                          'new_students': new_students}
                      )

    def post(self, request): # noqa

        teacher_form = TeacherForm(request.POST)
        teacher_form.save()
        teacher = Teacher.objects.last()

        return redirect(reverse('teacher_info', kwargs={"id": teacher.id}))


class CSVView(View):

    def get(self, request):
        response = HttpResponse(content_type="text/csv")

        response['Content-Disposition'] = \
            "attachment; filename=data_students.csv"
        writer_for_response = csv.writer(response)
        writer_for_response.writerow([
            "Name", "Age", "Sex", "Address", "Description",
            "B-day", "E-mail", "Book", "Subject", "Teacher"
        ])

        students = Student.objects.all()
        for student in students:
            teachers = ""
            for teacher in student.teacher_set.all():
                if teachers:
                    teachers += ",/n"
                teachers += teacher.name + " " + teacher.surname
            writer_for_response.writerow([
                student.name + " " + student.surname,
                student.age,
                student.sex,
                student.address,
                student.description,
                student.birthday,
                student.email,
                student.book.title if student.book else None,
                student.subject.name_of_subject if student.subject else None,
                teachers if teachers else None,
            ])

        return response


class JsonView(View):

    def get(self, request):

        students = Student.objects.all()

        return JsonResponse({
            "students": list(students.values(
                "name",
                "surname",
                "age",
                "sex",
                "address",
                "description",
                "birthday",
                "email",
                "book__title",
                "subject__name_of_subject",
                "teacher__name",
                "teacher__surname"
            )),
        })
