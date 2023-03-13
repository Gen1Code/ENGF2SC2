from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Questions, getAnswer
from .forms import QuestionForm, AnswerForm, LanguageForm, AnswerFormReturned
from django.shortcuts import render
from django.utils.translation import gettext as _
from django.utils import translation
from django import http
from django.conf import settings
from django_ajax.decorators import ajax
from SetClass import Set


def homePage(request):
    template = loader.get_template('homepage.html')
    return HttpResponse(template.render({}, request))


def createQuestionPage(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            # Change Answer from equation into list of regions
            question = Questions(
                Question=form.cleaned_data["Question"],
                Answer=form.cleaned_data["Answer"],
                Difficulty=form.cleaned_data["Difficulty"]
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
    'Size': question.Size,
    'form': AnswerForm()
  }
  return HttpResponse(template.render(context,request))

@ajax
def checkAnswer(request):
  if request.method == 'POST':
    form = AnswerFormReturned(request.POST)
    if form.is_valid():
      Answer = form.cleaned_data["Answer"]
      Question = form.cleaned_data["Question"]
      Size = form.cleaned_data["Size"]
      #Regex Check
      x = Set(int(Size))
      if x.regexCheck(Answer):
        if x.balancedParentheses(Answer):
          regions = x.evaluate(Answer)
          #Check Database if Answer is the same (Answer is stored as a list of regions in database)
          if regions == getAnswer(Question):
            return {"Result":True}

      #branch to different parts depending if correct or not
      #Make redirects
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
