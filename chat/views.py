from django.contrib.auth.models import User
from django.shortcuts import redirect, render


def index(request):
    if request.user.is_authenticated:
        return render(request, 'chat/profile.html', context={'username': request.user.username})
    return redirect('/login')

# TODO merge signup and check_signup
def signup(request):
    return render(request, 'registration/signup.html')


def check_signup(request):
    bad_signup = True
    username = request.POST['username']
    password = request.POST['password']
    password_repeat = request.POST['password_repeat']
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']

    if username and password and password == password_repeat and first_name and last_name:
        User.objects.create_user(username=username, password=password, first_name=first_name, last_name=last_name)
        bad_signup = False

    if bad_signup:
        return redirect('/signup')
    return redirect('/login')
