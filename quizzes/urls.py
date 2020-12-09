from rest_framework import routers
from django.urls import path
from . import views

router = routers.DefaultRouter()
router.register('questions', views.ListCreateQuestion)

urlpatterns = [
    path('listcreate/',views.ListCreateQuiz.as_view(),name='quiz_list'),
    path('<pk>/',views.RetrieveUpdateDestroyQuiz.as_view(),name='quiz_detail'),
    path('<quiz_pk>/questions/',views.ListCreateQuestion.as_view(),name='question_list'),
    path('<quiz_pk>/questions/<pk>/',views.RetrieveUpdateDestroyQuestion.as_view(),name='question_detail'),
    path('<quiz_pk>/questions/<question_pk>/answers/',views.ListCreateAnswer.as_view(),name='answer_list'),
    path('<quiz_pk>/questions/<questoin_pk>/answers/<pk>/',views.RetrieveUpdateDestroyAnswer.as_view(),name='answer_detail')
]


app_name = 'quizzes'