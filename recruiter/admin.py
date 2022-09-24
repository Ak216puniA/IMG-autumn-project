from django.contrib import admin
from .models import Users,RecruitmentSeasons,Rounds,Sections,Questions,Candidates,InterviewPanel,CandidateMarks,CandidateRound,CandidateProjectLink


admin.site.register(Users)
admin.site.register(RecruitmentSeasons)
admin.site.register(Rounds)
admin.site.register(Sections)
admin.site.register(Questions)
admin.site.register(Candidates)
admin.site.register(InterviewPanel)
admin.site.register(CandidateMarks)
admin.site.register(CandidateRound)
admin.site.register(CandidateProjectLink)
