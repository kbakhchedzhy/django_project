"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.decorators.cache import cache_page

from djangoProject import settings
from home.views import BookInfoView, BookListView, \
    StudentAddView, StudentListView, \
    StudentUpdateView, SubjectInfoView, \
    SubjectListView, TeacherInfoView, TeacherListView, TeacherAddView, CSVView, JsonView, SendMailView, \
    StudentDeleteView, SignUpView, ActivateView, SignInView, SignOutView  # noqa
# noqa
urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/', cache_page(settings.CACHE_TTL)(StudentListView.as_view())), # noqa
    path('students/add/', StudentAddView.as_view(), name='add'),
    path('students/update/<pk>', StudentUpdateView.as_view(), name='update'),
    path('student/delete/<pk>', StudentDeleteView.as_view(), name='delete'),
    path('books/', BookListView.as_view(), name='books_list'),
    path('books/<id>', BookInfoView.as_view(), name='book_info'),
    path('subjects/', SubjectListView.as_view(), name='subjects_list'),
    path('subjects/<id>', SubjectInfoView.as_view(), name='subject_info'),
    path('teachers/', TeacherListView.as_view(), name='teacher_list'),
    path('teachers/<id>', TeacherInfoView.as_view(), name='teacher_info'),
    path('teachers/add/', TeacherAddView.as_view(), name='teacher_add'),
    path('activate/<uid>/<token>', ActivateView.as_view(), name='activate_view'),
    path('login', SignInView.as_view(), name='login_view'),
    path('register/', SignUpView.as_view(), name='sign_up'),
    path('logout', SignOutView.as_view(), name='sign_out_view'),
    path('students/download/', CSVView.as_view(), name='csv_download'),
    path('students/json/', JsonView.as_view(), name='json_download'),
    path('sendmail/', SendMailView.as_view(), name='send_mail'),

]
