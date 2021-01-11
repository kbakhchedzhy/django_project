# Generated by Django 3.1.4 on 2021-01-11 12:56
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20210107_1416'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title_of_book', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name_of_subject', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('surname', models.CharField(max_length=200)),
                ('students', models.ManyToManyField(to='home.Student')),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='book',
            field=models.OneToOneField(null=True,
                                       on_delete=django.db.models.deletion.CASCADE, # noqa
                                       to='home.book'),
        ),
        migrations.AddField(
            model_name='student',
            name='subject',
            field=models.ForeignKey(null=True,
                                    on_delete=django.db.models.deletion.SET_NULL, # noqa
                                    to='home.subject'),
        ),
    ]
