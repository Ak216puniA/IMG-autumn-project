from rest_framework.response import Response
from .serializers import *
from .models import *
from rest_framework import viewsets
from rest_framework.views import APIView
import environ
import requests
from .user_auth import get_user_data,check_and_create_user,get_auth_code
from .permissions import YearWisePermission, SuperUserPermission
from rest_framework.permissions import AllowAny
from django.contrib.auth import login,logout

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
    permission_classes=[AllowAny]
    def get(self, request, format=None):
        view_response={
            'succesful' : False,
            'desc' : ''
        }

        token_url=env('AUTH_TOKEN_URL')
        request_data = {
            'grant_type':'authorization_code',
            'code' : request.query_params['code'],
            'redirect_url' : 'http://localhost:8000/auth/auth-token/',
            'client_id' : env('CLIENT_ID'),
            'client_secret' : env('CLIENT_SECRET'),
        }
        try:
            response_token = requests.post(url=token_url, data=request_data)
        # except exceptions.ConnectionError as e:
        #     message='Connection error when requesting for auth_token'
        #     desc=e
        # except exceptions.Timeout as e:
        #     message='Timeout when requesting for auth_token'
        #     desc=e
        # except exceptions.HTTPError as e:
        #     message='Invalid response when requesting for auth_token'
        #     desc=e
        # except Exception as e:
        #     message='Error occured when requesting for auth_token:'
        #     desc=e
        except Exception as e:
            view_response['succesful']=False
            view_response['desc']=e

        else:
            if response_token.status_code==200:
                view_response['succesful']=False
                view_response['desc']=response_token.json()

                AUTH_TOKEN = response_token.json()['access_token']
                AUTH_TOKEN_TYPE = response_token.json()['token_type']

                login_view_url = 'http://localhost:8000/auth/login/'
                token = AUTH_TOKEN_TYPE+' '+AUTH_TOKEN
                token_data={'token' : token}

                try:
                    response_login_view = requests.post(url=login_view_url, data=token_data)
                except Exception as e:
                    view_response['succesful']=False
                    view_response['desc']=e
                else:           
                    if response_login_view.status_code==200:
                        view_response['succesful']=True
                        view_response['desc']=response_login_view.json()

        return Response(view_response)

class LoginView(APIView):
    permission_classes=[AllowAny]

    def post(self, request, format=None):
        token = request.data['token']
        user_data = get_user_data(token)

        if user_data is not None:
            if user_data['is_maintainer']:
                user_dict = check_and_create_user(user_data)
                login(request,user_dict['user'])
        return Response(user_dict)  

class LogoutView(APIView):
    def get(self, request, format=None):
        if request.user.is_authenticated:
            logout(request)
            return Response({'logged_out':True})
        return Response({'logged_out':True})    
