# Generated by Django 3.1.5 on 2021-03-12 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0027_auto_20210312_1953'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='photo',
        ),
        migrations.AddField(
            model_name='teacher',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='pictures'), # noqa
        ),
    ]
