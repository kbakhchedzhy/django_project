from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic.base import View

from home.forms import StudentForm
from home.models import Student


class StudentListView(View):
    """
    Output list of students.
    """

    def get(self, request):

        students = Student.objects.all()
        students_list = StudentForm()

        return render(request, 'index.html',
                      context={
                          'students': students,
                          'form': students_list}
                      )


class StudentAddView(View):
    """
    Output forms for insert new students.
    """

    def get(self, request):
        students = Student.objects.all()
        students_list = StudentForm()

        return render(request, 'add_student.html',
                      context={
                          'students': students,
                          'form': students_list}
                      )

    def post(self, request):
        students_list = StudentForm(request.POST)
        students_list.save()
        return redirect(reverse('home'))


class StudentUpdateView(View):
    """
    Outputs fields with information about this student. Can update info.
    """

    def get(self, request, id):
        student = Student.objects.get(id=id)
        student_form = StudentForm(instance=student)
        context = {'form': student_form,
                   'student_id': student.id}
        return render(request, 'update.html', context=context)

    def post(self, request, id):
        student = Student.objects.get(id=id)
        student_form = StudentForm(request.POST, instance=student)
        if student_form.is_valid():
            student_form.save()
        return redirect(reverse('home'))
