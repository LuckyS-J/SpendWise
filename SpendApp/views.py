from django.shortcuts import render

# Create your views here.

def Home(request):
  return render(request, 'SpendApp/index.html')

def Register(request):
  return render(request, 'SpendAPp/register.html')
