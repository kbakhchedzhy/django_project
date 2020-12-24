from django.contrib import admin # noqa
from django.contrib.admin import ModelAdmin
from django.utils.html import format_html

from home.models import Student


class StudentAdmin(ModelAdmin):
    list_display = ('full_name', 'email', 'birthday')
    ordering = ('name',)

    def full_name(self, instance):
        if instance.social_url:
            # Correy Gomez has url
            return format_html("<a href = \"{}\">{} {}</a>", instance.social_url, instance.name, instance.surname)
        else:
            return "{} {}".format(instance.name, instance.surname)


admin.site.register(Student, StudentAdmin)
