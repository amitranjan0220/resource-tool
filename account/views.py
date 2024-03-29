from django.http import HttpResponse
from django.shortcuts import render ,redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    user = request.user
                    return render(request, 'home.html',{'user':user})
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})

def home(request):
    user = request.user
    return render(request, 'home.html',{'user':user})


def logout_view(request):
    logout(request)
    return redirect("login")