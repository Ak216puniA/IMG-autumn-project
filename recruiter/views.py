from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework import viewsets

class UsersModelViewSet(viewsets.ModelViewSet):
    queryset=Users.objects.all()
    serializer_class=UserSerializer

class RecruitmentSeasonsModelViewSet(viewsets.ModelViewSet):
    queryset=RecruitmentSeasons.objects.all()
    serializer_class=RecruitmentSeasonsSerializer

class RoundsModelViewSet(viewsets.ModelViewSet):
    queryset=Rounds.objects.all()
    serializer_class=RoundsSerializer

class SectionsModelViewSet(viewsets.ModelViewSet):
    queryset=Sections.objects.all()
    serializer_class=SectionsSerializer

class QuestionsModelViewSet(viewsets.ModelViewSet):
    queryset=Questions.objects.all()
    serializer_class=QuestionsSerializer

class InterviewPanelModelViewSet(viewsets.ModelViewSet):
    queryset=InterviewPanel.objects.all()
    serializer_class=InterviewPanelSerializer

class CandidatesModelViewSet(viewsets.ModelViewSet):
    queryset=Candidates.objects.all()
    serializer_class=QuestionsSerializer

class CandidateProjectLinkModelViewSet(viewsets.ModelViewSet):
    queryset=CandidateProjectLink.objects.all()
    serializer_class=CandidateProjectLinkSerializer

class CandidateRoundModelViewSet(viewsets.ModelViewSet):
    queryset=CandidateRound.objects.all()
    serializer_class=CandidateRoundSerializer

class CandidateMarksModelViewSet(viewsets.ModelViewSet):
    queryset=CandidateMarks.objects.all()
    serializer_class=CandidateMarksSerializer

#TO-DO : Views for authentication

