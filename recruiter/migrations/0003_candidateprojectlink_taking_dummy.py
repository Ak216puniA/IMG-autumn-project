# Generated by Django 4.1.1 on 2022-09-25 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recruiter', '0002_recruitmentseasons_rounds_sections_questions_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidateprojectlink',
            name='taking_dummy',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
