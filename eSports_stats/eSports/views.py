from django.shortcuts import render

# Create your views here.
def display_home(request):
    return render(request, 'landingPage/index.html')

def display_create(request):
    return render(request, 'create/index.html')

def display_dash(request):
    return render(request, 'dashboard/index.html')
