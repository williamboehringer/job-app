# Generated by Django 4.1.2 on 2022-11-03 21:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_jobpost_type_alter_jobpost_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobpost',
            name='location',
        ),
    ]
