# Generated by Django 3.1.5 on 2021-03-12 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0021_currency'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='picture',
            field=models.FileField(null=True, upload_to='student_photos/'),
        ),
    ]
