from django.db import models
from django.utils.translation import gettext_lazy as _

class Users(models.Model):
    username=models.CharField(max_length=255)
    useremail=models.EmailField(max_length=255)
    userpass=models.CharField(max_length=255)
    userpart=models.CharField(max_length=10)
    year=models.IntegerField()

class Recruitment_seasons(models.Model):
    academic_year=models.CharField(max_length=16)
    start=models.DateField(auto_now_add=True)
    end=models.DateField()

    class TypeOfSeason(models.TextChoices):
        DEVELOPER = 'developer', _('Developer')
        DESIGNER = 'designer', _('Designer')

    type=models.CharField(max_length=16,choices=TypeOfSeason.choices,blank=False,default=TypeOfSeason.DEVELOPER)

class Rounds(models.Model):
    season_id=models.ForeignKey(Recruitment_seasons,on_delete=models.CASCADE)
    name=models.CharField(max_length=255)

    class TypeOfRound(models.TextChoices):
        TEST = 'test', _('Test')
        INTERVIEW = 'interview', _('Interview')

    type=models.CharField(max_length=16,choices=TypeOfRound.choices,blank=False,default=TypeOfRound.TEST)

class Sections(models.Model):
    round_id=models.ForeignKey(Rounds,on_delete=models.CASCADE)
    name=models.CharField(max_length=255)
    weightage=models.IntegerField()
    assignee=models.ForeignKey(Users,on_delete=models.CASCADE)

class Questions(models.Model):
    section_id=models.ForeignKey(Sections,on_delete=models.CASCADE)
    text=models.TextField()
    marks=models.IntegerField()
    assignee=models.ForeignKey(Users,on_delete=models.CASCADE)

class Candidates(models.Model):
    season_id=models.ForeignKey(Recruitment_seasons,on_delete=models.CASCADE)
    name=models.CharField(max_length=255)
    email=models.EmailField(max_length=255)
    enrollment_no=models.IntegerField()
    mobile_no=models.CharField(max_length=16)
    cg=models.DecimalField(max_digits=2,decimal_places=2)
    round_id=models.ForeignKey(Rounds,on_delete=models.CASCADE)

class Interview_panel(models.Model):
    season_id=models.ForeignKey(Recruitment_seasons,on_delete=models.CASCADE)
    panel_name=models.CharField(max_length=64)
    panelist=models.ManyToManyField(Sections)
    location=models.CharField(max_length=64)

    class StatusOfPanel(models.TextChoices):
        OCCUPIED = 'occupied', _('Occupied')
        IDLE = 'idle', _('Idle')
        ON_BREAK = 'on_break', _('On Break')

    status=models.CharField(max_length=16,choices=StatusOfPanel.choices,default=StatusOfPanel.IDLE)

class Candidate_marks(models.Model):
    candidate_id=models.ForeignKey(Candidates,on_delete=models.CASCADE)
    question_id=models.ForeignKey(Questions,on_delete=models.CASCADE)
    marks=models.IntegerField()

    class StatusOfQuestion(models.TextChoices):
        CHECKED = 'checked', _('Checked')
        UNCHECKED= 'unchecked', _('Unchecked')

    status=models.CharField(max_length=16,choices=StatusOfQuestion.choices,default=StatusOfQuestion.UNCHECKED)

class Candidate_round(models.Model):
    candidate_id=models.ForeignKey(Candidates,on_delete=models.CASCADE)
    round_id=models.ForeignKey(Rounds,on_delete=models.CASCADE)
    remark=models.TextField()
    interview_panel=models.ManyToManyField(Interview_panel)
    time_slot=models.CharField(max_length=64)

    class StatusOfRound(models.TextChoices):
        NOT_NOTIFIED = 'not_notified', _('Not Notified')
        NOTIFIED = 'notified', _('Notified')
        WAITING_ROOM = 'waiting_room', _('In Waiting cRoom')
        INTERVIEW = 'interview', _('In Interview')
        DONE = 'done', _('Done')

    status=models.CharField(max_length=16,choices=StatusOfRound.choices,default=StatusOfRound.NOT_NOTIFIED)