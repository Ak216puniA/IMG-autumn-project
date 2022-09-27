from rest_framework.response import Response
from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework import viewsets
from rest_framework.views import APIView
import environ
import requests
from .user_auth import get_user_data,check_and_create_user
from .permissions import YearWisePermission, SuperUserPermission
from rest_framework.permissions import AllowAny

env = environ.Env()
environ.Env.read_env()

class UsersModelViewSet(viewsets.ModelViewSet):
    queryset=Users.objects.all()
    serializer_class=UserSerializer
    permission_classes=[SuperUserPermission]

class RecruitmentSeasonsModelViewSet(viewsets.ModelViewSet):
    queryset=RecruitmentSeasons.objects.all()
    serializer_class=RecruitmentSeasonsSerializer
    permission_classes=[YearWisePermission]

class RoundsModelViewSet(viewsets.ModelViewSet):
    queryset=Rounds.objects.all()
    serializer_class=RoundsSerializer
    permission_classes=[YearWisePermission]

class SectionsModelViewSet(viewsets.ModelViewSet):
    queryset=Sections.objects.all()
    serializer_class=SectionsSerializer
    permission_classes=[YearWisePermission]

class QuestionsModelViewSet(viewsets.ModelViewSet):
    queryset=Questions.objects.all()
    serializer_class=QuestionsSerializer
    permission_classes=[YearWisePermission]

class InterviewPanelModelViewSet(viewsets.ModelViewSet):
    queryset=InterviewPanel.objects.all()
    serializer_class=InterviewPanelSerializer
    permission_classes=[YearWisePermission]

class CandidatesModelViewSet(viewsets.ModelViewSet):
    queryset=Candidates.objects.all()
    serializer_class=QuestionsSerializer
    permission_classes=[YearWisePermission]

class CandidateProjectLinkModelViewSet(viewsets.ModelViewSet):
    queryset=CandidateProjectLink.objects.all()
    serializer_class=CandidateProjectLinkSerializer
    permission_classes=[YearWisePermission]

class CandidateRoundModelViewSet(viewsets.ModelViewSet):
    queryset=CandidateRound.objects.all()
    serializer_class=CandidateRoundSerializer
    permission_classes=[YearWisePermission]

class CandidateMarksModelViewSet(viewsets.ModelViewSet):
    queryset=CandidateMarks.objects.all()
    serializer_class=CandidateMarksSerializer
    permission_classes=[YearWisePermission]

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

            login_view_url = 'http://localhost:8000/auth/login/'
            token = AUTH_TOKEN_TYPE+' '+AUTH_TOKEN
            token_data={'token' : token}

            response_login_view = requests.post(url=login_view_url, data=token_data)

            if response_login_view.status_code==200:
                return Response(response_login_view.json())
            return Response(response_login_view.json())
        return Response(response_token.json())

    permission_classes=[AllowAny]

class LoginView(APIView):
    def post(self, request, format=None):
        token = request.data['token']
        user_data = get_user_data(token)

        if user_data is not None:
            if user_data['is_maintainer']:
                new_user = check_and_create_user(user_data)
        return Response({'New user created':new_user, 'User data':user_data})

    permission_classes=[AllowAny]

# TO-DO : Exception handling