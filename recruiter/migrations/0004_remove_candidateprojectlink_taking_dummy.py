# Generated by Django 4.1.1 on 2022-09-25 02:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recruiter', '0003_candidateprojectlink_taking_dummy'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidateprojectlink',
            name='taking_dummy',
        ),
    ]
