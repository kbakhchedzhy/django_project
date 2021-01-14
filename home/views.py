from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic.base import View

from home.forms import StudentForm, SubjectForm, TeacherForm
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
        students = Student.objects.all()
        students_list = StudentForm()

        return render(request, 'student_add.html',
                      context={
                          'students': students,
                          'form': students_list}
                      )

    def post(self, request): # noqa
        students_list = StudentForm(request.POST)
        students_list.save()
        return redirect(reverse('home'))


class StudentUpdateView(View):
    """
    Outputs fields with information about this student. Can update info.
    """

    def get(self, request, id): # noqa
        student = Student.objects.get(id=id)
        student_form = StudentForm(instance=student)
        context = {'form': student_form,
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

        return redirect(reverse('teacher_list'))
