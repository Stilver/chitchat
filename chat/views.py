from django.http import HttpResponse
from django.shortcuts import redirect, render


def index(request):
    if request.user.is_authenticated:
        return render(request, 'chat/profile.html', context={'username': request.user.username})
    return redirect('/login')


def signup(request):
    return render(request, 'registration/signup.html')
