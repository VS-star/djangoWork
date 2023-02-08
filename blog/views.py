from django.shortcuts import render
from django.http import HttpResponse

# This is function-based view.
def home(request):
  return HttpResponse('<h1>Blog Home</h1>')

def about(request):
  return HttpResponse('<h1>This is about page for a Blog</h1>')
