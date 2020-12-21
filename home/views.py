from django.http import HttpResponse


def home(request):
    """
    Page /home.
    :return: string 'Hello world!'
    """
    return HttpResponse('<h1>Hello world!</h1>')
