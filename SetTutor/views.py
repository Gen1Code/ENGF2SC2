from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Questions
from .forms import QuestionForm, AnswerForm, LanguageForm
from django.shortcuts import render
from django.utils.translation import gettext as _
from django.utils import translation
from django import http
from django.conf import settings

def homePage(request):
  template = loader.get_template('homepage.html')
  return HttpResponse(template.render({},request))

def createQuestionPage(request):
  if request.method == 'POST':
    form = QuestionForm(request.POST)
    if form.is_valid():
      #Change Answer from equation into list of regions
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
    'form': AnswerForm()
  }
  return HttpResponse(template.render(context,request))

def checkQuestionPage(request):
  if request.method == 'POST':
    form = AnswerForm(request.POST)
    if form.is_valid():
      Answer = form.cleaned_data["Answer"]
      #Regex Check
      #balanced Paranthesis Check
      #Turn equation into List of Regions
      #Check Database if Answer is the same (Answer is stored as a list of regions in database)
      #branch to different parts depending if correct or not
      #Make redirects
      return HttpResponseRedirect('/')
  else:
    return HttpResponse('/')

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