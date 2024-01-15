# from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from pip._internal.network.session import user_agent


# Create your views here.
def home(request):
    # return HttpResponse('<h1>Hello  word</h1>')
    return render(request, 'home.html')


def signup(request):
    # return HttpResponse('<h1>Hello  word</h1>')
    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'],
                                                password=request.POST['password2'])
                user.save()
                return HttpResponse('User create successful')
            except:
                return HttpResponse('User already exist')
        return HttpResponse('Password do not much')
