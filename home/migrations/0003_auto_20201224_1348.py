# Generated by Django 3.1.4 on 2020-12-24 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_student_social_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='social_url',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
