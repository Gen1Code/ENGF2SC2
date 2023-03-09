from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage, name='homePage'),
    path('question', views.questionPage, name="questionPage"),
    path('createquestion', views.createQuestionPage, name="createQuestionPage"),
    path('checkquestion', views.checkQuestionPage, name="checkQuestion")
]