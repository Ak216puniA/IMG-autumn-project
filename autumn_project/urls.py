from django.contrib import admin
from django.urls import path,include
from recruiter import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('recruitment_season',views.RecruitmentSeasonsModelViewSet ,basename='season')
router.register('round',views.RoundsModelViewSet ,basename='round')
router.register('section',views.SectionsModelViewSet ,basename='section')
router.register('question',views.QuestionsModelViewSet ,basename='question')
router.register('user',views.UsersModelViewSet ,basename='user')
router.register('candidate',views.CandidatesModelViewSet ,basename='candidate')
router.register('interview_panel',views.InterviewPanelModelViewSet ,basename='interview_panel')
router.register('candidate_round',views.CandidateRoundModelViewSet ,basename='candidate_round')
router.register('candidate_marks',views.CandidateMarksModelViewSet ,basename='candidate_marks')
router.register('candidate_link',views.CandidateProjectLinkModelViewSet ,basename='candidate_link')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', include(router.urls)),
    path('auth/auth-token/', views.GetAuthTokenView.as_view()),
    path('auth/login/', views.LoginView.as_view())
]
