from django.contrib import admin
from .models import *


# admin.site.register(Users)
# admin.site.register(RecruitmentSeasons)
# admin.site.register(Rounds)
# admin.site.register(Sections)
# admin.site.register(Questions)
# admin.site.register(Candidates)
# admin.site.register(InterviewPanel)
# admin.site.register(CandidateMarks)
# admin.site.register(CandidateRound)
# admin.site.register(CandidateProjectLink)

@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = ['id','username','userpart','year']

@admin.register(RecruitmentSeasons)
class RecruitmentSeasonsAdmin(admin.ModelAdmin):
    list_display = ['id','name','type','start']

@admin.register(Rounds)
class RoundsAdmin(admin.ModelAdmin):
    list_display = ['id','season_id','name','type']

@admin.register(Sections)
class SectionsAdmin(admin.ModelAdmin):
    list_display = ['id','round_id','name']

@admin.register(Questions)
class QuestionsAdmin(admin.ModelAdmin):
    list_display = ['id','section_id','text','marks']

@admin.register(Candidates)
class CandidatesAdmin(admin.ModelAdmin):
    list_display = ['id','name','enrollment_no','current_round_id']

@admin.register(CandidateProjectLink)
class CandidateProjectLinkAdmin(admin.ModelAdmin):
    list_display = ['id','candidate_id','link']

@admin.register(InterviewPanel)
class InterviewPanelAdmin(admin.ModelAdmin):
    list_display = ['id','season_id','panel_name','location']

@admin.register(CandidateRound)
class CandidateRoundAdmin(admin.ModelAdmin):
    list_display = ['id','candidate_id','round_id','status']

@admin.register(CandidateMarks)
class CandidateMarksAdmin(admin.ModelAdmin):
    list_display = ['id','candidate_id','question_id','status','marks']