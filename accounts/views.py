from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout

# Create your views here.
def subscribe(request):
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            user =  form.save()
            login(request, user) 
            return redirect('/')
    else:
        return render(request, 'accounts/subscribe.html', context={'form': UserCreationForm()})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
    else:
        form = AuthenticationForm()
        return render(request, 'accounts/login.html', {'form': form})
        

def logout_view(request):
    if request.method == 'POST':
        logout(request)
    return HttpResponse('deslogou')

