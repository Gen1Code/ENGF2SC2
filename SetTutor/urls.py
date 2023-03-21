from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage, name='homePage'),
    path('setlanguage', views.setLanguage, name="setlanguage"),
    path('question', views.questionPage, name="questionPage"),
    path('createQuestion', views.createQuestionPage, name="createQuestionPage"),
    path('ajax/checkAnswer', views.checkAnswer, name="checkAnswer")
]