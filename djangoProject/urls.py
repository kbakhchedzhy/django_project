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

from home.views import BookInfoView, BookListView, \
    StudentAddView, StudentListView, \
    StudentUpdateView, SubjectInfoView, \
    SubjectListView, TeacherInfoView, TeacherListView, TeacherAddView  # noqa
# noqa
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', StudentListView.as_view(), name='home'),
    path('add/', StudentAddView.as_view(), name='add'),
    path('update/<id>', StudentUpdateView.as_view(), name='update'),
    path('books/', BookListView.as_view(), name='books_list'),
    path('books/<id>', BookInfoView.as_view(), name='book_info'),
    path('subjects/', SubjectListView.as_view(), name='subjects_list'),
    path('subjects/<id>', SubjectInfoView.as_view(), name='subject_info'),
    path('teachers/', TeacherListView.as_view(), name='teacher_list'),
    path('teachers/<id>', TeacherInfoView.as_view(), name='teacher_info'),
    path('teachers/add/', TeacherAddView.as_view(), name='teacher_add'),
]
