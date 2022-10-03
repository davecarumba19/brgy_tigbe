from django.shortcuts import render, redirect

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from django.contrib import messages
from .models import Profiles
from main.models import News, Events
from .forms import CustomUserCreationForm, ProfileForm, ReportsForm


# Create your views here.

def loginUser(request):
    page = 'login'

    if request.user.is_authenticated:
        return redirect('main-page')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.warning(request, 'User does not Exist!')
        
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Login Successfully!')
            return redirect('account')
        else:
            messages.warning(request, 'Username or Password is incorrect!')

    return render(request, 'profiles/login-register.html')

def logoutUser(request):
    logout(request)
    return redirect('login')

def registerUser(request):
    page = 'register'
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request, 'User has been created!')
            login(request, user)
            return redirect('account')
        else:
            messages.error(request, 'Error has been accurred!')

    context = {
        'page':page,
        'form':form,
    }
    return render(request, 'profiles/login-register.html', context)


@login_required(login_url='login')
def userProfile(request, pk):
    profile = Profiles.objects.get(id=pk)

    context = {
        'profile': profile,
    }
    return render(request, 'profiles/profiles.html', context)

@login_required(login_url='login')
def userAccount(request):

    profile = request.user.profiles

    newsObj = News.objects.all().order_by('-date_created')
    eventsObj = Events.objects.all().order_by('-date_created')[:3]

    context = {
        'profile': profile,
        'newsObj': newsObj,
        'eventsObj': eventsObj,
    }
    return render(request, 'profiles/account.html', context)


login_required(login_url='login')
def editAccount(request):
    profile = request.user.profiles
    form = ProfileForm(instance=profile)
    
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('account')

    context = {
        'form': form,
    }
    return render(request, 'profiles/edit-account.html', context)


@login_required(login_url='login')
def searchAccount(request):
    search_account = ''

    if request.GET.get('searchAccount'):
        search_account = request.GET.get('searchAccount')
    
    profiles = Profiles.objects.filter(first_name__icontains=search_account)

    context = {
        'profiles':profiles
    }
    return render(request, 'profiles/search-account.html', context)

def loginAdmin(request):

    if request.user.is_authenticated:
        return redirect('main-page')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = User.objects.filter(username='dave')
        try:
            user.get(username=username)
        except:
            messages.warning(request, 'User does not Exist!')
            return redirect('login-admin')
        
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Login Successfully!')
            return redirect('account')
        else:
            messages.warning(request, 'Username or Password is incorrect!')

    context = {
        
    }
    return render(request, 'profiles/admin-login.html', context)

def reportConcern(request):

    profile = request.user.profiles
    form = ReportsForm()

    if request.method == 'POST':
        form = ReportsForm(request.POST)
        if form.is_valid():
            report = form.save(commit=False)
            report.owner = profile
            report.save()
            return redirect('account')

    context = {
        'form':form,
    }
    return render(request, 'profiles/reports.html', context)