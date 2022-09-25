from rest_framework import serializers
from .models import *

# User model serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['id','username','email','password','userpart','year','image','is_active']
        extra_kwargs = {
            'password':{ 'write_only' : True }
        }

class UserNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['id','username']


# RecruitmentSeasons model serializers

class RecruitmentSeasonsSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecruitmentSeasons
        fields = '__all__'

class RecruitmentSeasonsNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecruitmentSeasons
        fields = ['id','name']


# Rounds model serializers

class RoundsSerializer(serializers.ModelSerializer):
    season_id = RecruitmentSeasonsNameSerializer()
    class Meta:
        model = Rounds
        fields = '__all__'

class RoundsNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rounds
        fields = ['id','name']


# Sections model serializers

class SectionsSerializer(serializers.ModelSerializer):
    round_id = RoundsNameSerializer()
    class Meta:
        model = Sections
        fields = '__all__'

class SectionsNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sections
        fields = ['id','name']


# Questions model serializers

class QuestionsSerializer(serializers.ModelSerializer):
    section_id = SectionsNameSerializer()
    class Meta:
        model = Questions
        fields = '__all__'

class QuestionsNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questions
        fields = '__all__'
        exclude = ['assignee']


# Candidates model serializers

class CandidatesSerializer(serializers.ModelSerializer):
    current_round_id = RoundsNameSerializer()
    class Meta:
        model = Candidates
        fields = '__all__'

class CandidatesNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidates
        fields = ['id','name']


# InterviewPanel model serializers

class InterviewPanelSerializer(serializers.ModelSerializer):
    season_id = RecruitmentSeasonsNameSerializer()
    panelist = UserNameSerializer(many=True)
    class Model:
        model = InterviewPanel
        fields = '__all__'

class InterviewPanelNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = InterviewPanel
        fields = ['panel_name']


# CandidateMarks model serializers

class CandidateMarksSerializer(serializers.ModelSerializer):
    candidate_id = CandidatesNameSerializer()
    question_id = QuestionsNameSerializer()
    class Meta:
        model = CandidateMarks
        fields = '__all__'


# CandidateRound model serializers

class CandidateRoundSerializer(serializers.ModelSerializer):
    candidate_id = CandidatesNameSerializer()
    round_id = RoundsNameSerializer()
    interview_panel = InterviewPanelNameSerializer()
    class Meta:
        model = CandidateRound
        fields = '__all__'


# CandidateProjectLink model serializers

class CandidateProjectLinkSerializer(serializers.ModelSerializer):
    candidate_id = CandidatesNameSerializer()
    class Meta:
        model = CandidateProjectLink
        fields = '__all__'