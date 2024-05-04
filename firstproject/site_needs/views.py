from django.http import HttpResponse
from django.template import loader

def members(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())

def Schedule(request):
  template = loader.get_template('Schedule.html')
  return HttpResponse(template.render())

def Resources(request):
  template = loader.get_template('Resources.html')
  return HttpResponse(template.render())

def Budget(request):
  template = loader.get_template('Budget.html')
  return HttpResponse(template.render())