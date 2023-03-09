from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Questions
from .forms import QuestionForm, AnswerForm
from django.shortcuts import render

def homePage(request):
  template = loader.get_template('homepage.html')
  return HttpResponse(template.render())

def createQuestionPage(request):
  if request.method == 'POST':
    form = QuestionForm(request.POST)
    if form.is_valid():
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
    'Answer': question.Answer,
    'Difficulty': question.Difficulty,
    'form': AnswerForm()
  }
  return HttpResponse(template.render(context,request))

def checkQuestionPage(request):
  if request.method == 'POST':
    form = AnswerForm(request.POST)
    if form.is_valid():
      Answer = form.cleaned_data["Answer"]
      #check if correct
      #branch to different parts
      #Make redirects
      return HttpResponseRedirect('/')
  else:
    return HttpResponse('/')

