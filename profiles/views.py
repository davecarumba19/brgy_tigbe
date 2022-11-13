from django.shortcuts import render, redirect

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from django.contrib import messages
from .models import Profiles
from main.models import News, Events
from .forms import CustomUserCreationForm, ProfileForm, ReportsForm, RequestsForm, MessageForm, VerificationForm, VerifyProfileForm


# Create your views here.

def loginUser(request):
    page = 'login'

    if request.user.is_authenticated:
        return redirect('account')

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
            messages.warning(request, 'Error has been accurred!')
            messages.warning(request, 'Your password can’t be too similar to your other personal information.')
            messages.warning(request, 'Your password must contain at least 8 characters.')
            messages.warning(request, 'Your password can’t be a commonly used password.')
            messages.warning(request, 'Your password can’t be entirely numeric.')

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


@login_required(login_url='login')
def editAccount(request):
    profile = request.user.profiles
    form = ProfileForm(instance=profile)
    
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)
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
        return redirect('account')

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


@login_required(login_url='login')
def inbox(request):
    profile = request.user.profiles
    requestDocument = profile.request.all()
    reportConcern = profile.report.all()
    sendMessage = profile.message.all()
    verifyMessage = profile.verification.all()
    unreadCountDocument = requestDocument.filter(is_read=False).count()
    unreadCountReport = reportConcern.filter(is_read=False).count()
    unreadMessage = sendMessage.filter(is_read=False).count()
    unreadVerification = verifyMessage.filter(is_read=False).count()

    context = {
        'requestDocument': requestDocument,
        'reportConcern': reportConcern,
        'sendMessage': sendMessage,
        'verifyMessage': verifyMessage,
        'unreadCountDocument': unreadCountDocument,
        'unreadCountReport': unreadCountReport,
        'unreadMessage': unreadMessage,
        'unreadVerification': unreadVerification,
        'profile': profile,
    }
    return render(request, 'profiles/inbox.html', context)


@login_required(login_url='login')
def requestMessage(request, pk):
    profile = request.user.profiles
    requestMessage = profile.request.get(id=pk)

    if requestMessage.is_read == False:
        requestMessage.is_read = True
        requestMessage.save()

    context = {
        'requestMessage':requestMessage
    }
    return render(request, 'profiles/request-message.html', context)


@login_required(login_url='login')
def reportMessage(request, pk):
    profile = request.user.profiles
    reportMessage = profile.report.get(id=pk)

    if reportMessage.is_read == False:
        reportMessage.is_read = True
        reportMessage.save()

    context = {
        'reportMessage': reportMessage
    }
    return render(request, 'profiles/reports-message.html', context)


@login_required(login_url='login')
def verifyMessage(request, pk):
    profile = request.user.profiles
    verifyMessage = profile.verification.get(id=pk)

    if verifyMessage.is_read == False:
        verifyMessage.is_read = True
        verifyMessage.save()

    context = {
        'verifyMessage':verifyMessage,
    }
    return render(request, 'profiles/verify-message.html', context)



@login_required(login_url='login')
def reportConcern(request):
    profile = request.user.profiles
    receiver = Profiles.objects.get(id='d26b5cd8-0c06-4c7a-b1ac-030894b5e356')
    form = ReportsForm()

    if request.method == 'POST':
        form = ReportsForm(request.POST)
        if form.is_valid():
            report = form.save(commit=False)
            report.sender = profile
            report.receiver = receiver

            report.save()
            return redirect('account')

    context = {
        'form':form,
    }
    return render(request, 'profiles/reports.html', context)


@login_required(login_url='login')
def requestDocument(request):
    profile = request.user.profiles
    receiver = Profiles.objects.get(id='d26b5cd8-0c06-4c7a-b1ac-030894b5e356')
    form = RequestsForm()

    if request.method == 'POST':
        form = RequestsForm(request.POST)
        if form.is_valid():
            request = form.save(commit=False)
            request.sender = profile
            request.receiver = receiver

            request.save()
            return redirect('account')

    context = {
        'form':form,
    }
    return render(request, 'profiles/request.html', context)



@login_required(login_url='login')
def verifyAccount(request):
    profile = request.user.profiles
    receiver = Profiles.objects.get(id='d26b5cd8-0c06-4c7a-b1ac-030894b5e356')
    form = VerificationForm()

    if request.method == 'POST':
        form = VerificationForm(request.POST, request.FILES)
        if form.is_valid():
            verify = form.save(commit=False)
            verify.sender = profile
            verify.receiver = receiver

            verify.save()
            return redirect('account')

    context = {
        'form':form,
    }
    return render(request, 'profiles/verify.html', context)


@login_required(login_url='login')
def verified(request, pk):
    profile = Profiles.objects.get(id=pk)

    form = VerifyProfileForm(instance=profile)

    if request.method == 'POST':
        form = VerifyProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()

            return redirect('account')

    context = {
        'form':form,
    }
    return render(request, 'profiles/verified.html', context)



@login_required(login_url='login')
def createMessage(request, pk):
    profile = request.user.profiles
    receiver = Profiles.objects.get(id=pk)
    form = MessageForm()

    if request.method == 'POST':
        form = MessageForm(request.POST, request.FILES)
        if form.is_valid():
            send_message = form.save(commit=False)
            send_message.sender = profile
            send_message.receiver = receiver

            send_message.save()
            return redirect('account')

    context = {
        'form': form,
    }
    return render(request, 'profiles/create-message.html', context)


@login_required(login_url='login')
def viewMessage(request, pk):
    profile = request.user.profiles
    sendMessage = profile.message.get(id=pk)

    if sendMessage.is_read == False:
        sendMessage.is_read = True
        sendMessage.save()

    context = {
        'sendMessage':sendMessage
    }
    return render(request, 'profiles/view-message.html', context)

