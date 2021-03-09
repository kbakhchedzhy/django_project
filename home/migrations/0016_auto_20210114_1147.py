# Generated by Django 3.1.4 on 2021-01-14 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_auto_20210113_1912'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='teacher',
        ),
        migrations.AddField(
            model_name='teacher',
            name='students',
            field=models.ManyToManyField(to='home.Student'),
        ),
    ]