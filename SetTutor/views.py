from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Questions, getAnswer
from .forms import QuestionForm, LanguageForm, AnswerFormReturned
from django.shortcuts import render
from django.utils.translation import gettext as _
from django.utils import translation
from django import http
from django.conf import settings
from django_ajax.decorators import ajax
from SetClass import Set

SIMPLIFY_TYPE = 1
DIAGRAM_TYPE = 2

def homePage(request):
    template = loader.get_template('homepage.html')
    return HttpResponse(template.render({}, request))

def createQuestionPage(request):
  if request.method == 'POST':
    form = QuestionForm(request.POST)
    if form.is_valid():
      # Change Answer from equation into list of regions
      Q = form.cleaned_data["Question"]
      D = form.cleaned_data["Difficulty"]
      T = form.cleaned_data["Type"]
      x = Set(D)

      if T == DIAGRAM_TYPE:
        if not x.regexCheck(Q) or not x.balancedParentheses(Q):
          return HttpResponseRedirect('/')        

      question = Questions(
          Question=Q,
          Difficulty=D,
          Type=T
      )
      question.save()

      return HttpResponseRedirect('/')
  else:
      form = QuestionForm()
  return render(request, 'CreateQuestion.html', {'form': form})

def questionPage(request):
  question = Questions.objects.random()
  template = loader.get_template('questionpage.html')
  context = {
    'Question': question.Question,
    'Difficulty': question.Difficulty,
    'Type':question.Type
  }
  return HttpResponse(template.render(context,request))

@ajax
def checkAnswer(request):
  if request.method == 'POST':
    form = AnswerFormReturned(request.POST)
    if form.is_valid():
      Question = form.cleaned_data["Question"]
      Difficulty = form.cleaned_data["Difficulty"]
      Type = form.cleaned_data["Type"]
      Answer = form.cleaned_data["Answer"]

      if correctAnswer(Question,Difficulty,Type,Answer):
        return {"Result":True}

      return {"Result":False}
  else:
    return {"Error":""}


def setLanguage(request):
    if request.method == 'POST':
        form = LanguageForm(request.POST)
        if form.is_valid():
            language = form.cleaned_data["Language"]
            next = form.cleaned_data["next"]
            translation.activate(language)
            response = http.HttpResponseRedirect(next)
            response.set_cookie(settings.LANGUAGE_COOKIE_NAME, language)
            return response
    return HttpResponseRedirect('/')

def correctAnswer(Question,Difficulty,Type,Answer):
  x = Set(Difficulty)
  if Type == SIMPLIFY_TYPE:
    if not x.regexCheck(Answer) or not x.balancedParentheses(Answer):
       return False
    return x.evaluate(Answer) == Question
  elif Type == DIAGRAM_TYPE:
    #Check for answer is {...}
    return x.evaluate(Question) == Answer
  