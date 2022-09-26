from rest_framework.response import Response
from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework import viewsets
from rest_framework.views import APIView
import environ
import requests

env = environ.Env()
environ.Env.read_env()

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

class GetAuthTokenView(APIView):
    def get(self, request, code, format=None):
        token_url=env('AUTH_TOKEN_URL')
        request_data = {
            'grant_type':'authorization_code',
            'code' : code,
            'redirect_uri' : 'http://localhost:8000/auth/auth-token/',
            'client_id' : env('CLIENT_ID'),
            'client_secret' : env('CLIENT_SECRET'),
        }
        response_token = requests.post(url=token_url, data=request_data)

        if response_token.status_code==200:
            AUTH_TOKEN = response_token.json()['access_token']
            AUTH_TOKEN_TYPE = response_token.json()['token_type']

            user_data_url = env('USER_DATA_URL')
            headers = { 'Authentication' : AUTH_TOKEN_TYPE+' '+AUTH_TOKEN}

            response_user_data = requests.get(url=user_data_url, headers=headers)






class LoginView(APIView):
    def get(self,request):
        return Response({'msg':'Here is your request'})