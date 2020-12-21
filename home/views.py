from home.forms import StudentForm
from home.models import Student
from django.shortcuts import redirect, render


def home(request):
    """
    Page /home.
    :return: string 'Hello world!'
    """

    if request.method == 'GET':
        students = Student.objects.all()
        students_list = StudentForm()

        return render(request, 'index.html',
                      context={
                          'students': students,
                          'form': students_list}
                      )

    elif request.method == 'POST':
        students_list = StudentForm(request.POST)
        students_list.save()
        return redirect('/home/')
