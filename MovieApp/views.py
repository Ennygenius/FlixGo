from django.shortcuts import render, redirect
import requests
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import CreatingUserForm, LoginForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    URI = 'http://localhost:7000/api/movies'
    response = requests.get(URI)
    movies = response.json()
    newMovies = NewMovieModel.objects.all()
    context={'movies':movies, 'newMovies':newMovies}

    return render(request, 'index.html', context)


@login_required(login_url='/signin')
def movie_details(request,pk):
    newMovie = NewMovieModel.objects.get(id=pk)
    newMovies = NewMovieModel.objects.all()
    context={
        'newMovies':newMovies,
        'newMovie':newMovie
        }
    return render(request, 'details1.html', context)
    


def signup(request):
    form = CreatingUserForm()
    if request.method == "POST":
        form = CreatingUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('signin')
    return render(request, 'signup.html', {"form":form})


def signin(request):
        if request.method == 'POST':
            username = request.POST["username"]
            password = request.POST['password']
            user = authenticate(request, username=username,password=password)
            if user is not None:
                login(request, user)
                # messages.success(request, f'welcome {username}')
                return redirect('index')
            else:
                # messages.info(request, f'Accounts do not exist please signin!') 
                return redirect('signin')
        form = LoginForm()
        return render(request, 'signin.html', {"form":form})




def catalog(request):
     return render(request, 'catalog1.html')

def about(request):
     return render(request, 'about.html')

def logout_view(request):
    logout(request)
    return redirect('index')