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
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi  # noqa
from drf_yasg.views import get_schema_view
from rest_framework import permissions, routers  # noqa

from home.views import BookInfoView, BookListView, \
    StudentAddView, StudentListView, \
    StudentUpdateView, SubjectInfoView, \
    SubjectListView, TeacherInfoView, TeacherListView, TeacherAddView, CSVView, JsonView, SendMailView, \
    StudentDeleteView, SignUpView, ActivateView, SignInView, SignOutView, StudentViewSet, SubjectViewSet, \
    TeacherViewSet, BookViewSet  # noqa
# noqa

schema_view = get_schema_view(
   openapi.Info(
      title="Students Homework API",
      default_version='v1',
      description="Hillel homework for our students",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


router = routers.DefaultRouter()
router.register(r'students/view_set', StudentViewSet,
                basename='students_api')
router.register(r'subject/view_set', SubjectViewSet,
                basename='subject_api')
router.register(r'teacher/view_set', TeacherViewSet,
                basename='teacher_api')
router.register(r'book/view_set', BookViewSet,
                basename='report_card_api')

urlpatterns = [

    url(r'^swagger(?P<format>\.json|\.yaml)',
        schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/', schema_view.with_ui('swagger', cache_timeout=0),
        name='schema-swagger-ui'),
    url(r'^redoc/', schema_view.with_ui('redoc', cache_timeout=0),
        name='schema-redoc'),


    path('drf/', include(router.urls)),

    path('admin/', admin.site.urls),
    # path('students/', cache_page(settings.CACHE_TTL)(StudentListView.as_view())), # noqa
    path('students/', StudentListView.as_view(), name='home'), # noqa
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
    path('activate/<uid>/<token>', ActivateView.as_view(), name='activate_view'), # noqa
    path('login', SignInView.as_view(), name='login_view'),
    path('register/', SignUpView.as_view(), name='sign_up'),
    path('logout', SignOutView.as_view(), name='sign_out_view'),
    path('students/download/', CSVView.as_view(), name='csv_download'),
    path('students/json/', JsonView.as_view(), name='json_download'),
    path('sendmail/', SendMailView.as_view(), name='send_mail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
