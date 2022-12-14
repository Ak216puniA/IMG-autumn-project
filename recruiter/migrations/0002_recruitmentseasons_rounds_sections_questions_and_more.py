# Generated by Django 4.1.1 on 2022-09-25 02:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recruiter', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecruitmentSeasons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16)),
                ('start', models.DateField(auto_now_add=True)),
                ('end', models.DateField()),
                ('description', models.TextField()),
                ('type', models.CharField(choices=[('developer', 'Developer'), ('designer', 'Designer')], default='developer', max_length=16)),
                ('image', models.ImageField(null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Rounds',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('type', models.CharField(choices=[('test', 'Test'), ('interview', 'Interview')], default='test', max_length=16)),
                ('season_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recruiter.recruitmentseasons')),
            ],
        ),
        migrations.CreateModel(
            name='Sections',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('weightage', models.IntegerField()),
                ('round_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recruiter.rounds')),
            ],
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('marks', models.IntegerField()),
                ('assignee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('section_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recruiter.sections')),
            ],
        ),
        migrations.CreateModel(
            name='InterviewPanel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('panel_name', models.CharField(max_length=64)),
                ('location', models.CharField(max_length=64)),
                ('status', models.CharField(choices=[('occupied', 'Occupied'), ('idle', 'Idle'), ('on_break', 'On Break')], default='idle', max_length=16)),
                ('panelist', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
                ('season_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recruiter.recruitmentseasons')),
            ],
        ),
        migrations.CreateModel(
            name='Candidates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('enrollment_no', models.IntegerField()),
                ('mobile_no', models.CharField(max_length=16)),
                ('cg', models.DecimalField(decimal_places=2, max_digits=2)),
                ('current_round_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recruiter.rounds')),
            ],
        ),
        migrations.CreateModel(
            name='CandidateRound',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('remark', models.TextField()),
                ('time_slot', models.CharField(max_length=64)),
                ('total_marks', models.IntegerField()),
                ('status', models.CharField(choices=[('not_notified', 'Not Notified'), ('notified', 'Notified'), ('waiting_room', 'In Waiting Room'), ('interview', 'In Interview'), ('done', 'Done')], default='not_notified', max_length=16)),
                ('candidate_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recruiter.candidates')),
                ('interview_panel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recruiter.interviewpanel')),
                ('round_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recruiter.rounds')),
            ],
        ),
        migrations.CreateModel(
            name='CandidateProjectLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.TextField()),
                ('candidate_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recruiter.candidates')),
            ],
        ),
        migrations.CreateModel(
            name='CandidateMarks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marks', models.IntegerField()),
                ('remarks', models.TextField()),
                ('status', models.CharField(choices=[('checked', 'Checked'), ('unchecked', 'Unchecked')], default='unchecked', max_length=16)),
                ('candidate_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recruiter.candidates')),
                ('question_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recruiter.questions')),
            ],
        ),
    ]
