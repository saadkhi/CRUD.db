from django.shortcuts import render


# Create your views here.
def homepage(request):
    return render(request, 'website/homepage.html')

def login(request):
    return render(request, 'website/login.html')
