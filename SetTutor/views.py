from django.http import HttpResponse
from django.template import loader

def homePage(request):
  template = loader.get_template('homepage.html')
  return HttpResponse(template.render())