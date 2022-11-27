from django.shortcuts import render, redirect
from .models import News, Events, BrgyOfficials, SkOfficials
from .forms import NewsForm, EventsForm
from django.contrib.auth.decorators import login_required
# Create your views here.


def mainPage(request):
    newsObj = News.objects.all().order_by('-date_created')
    carouselNews = News.objects.all().order_by('-date_created')[:2]
    eventsObj = Events.objects.all().order_by('-date_created')

    context = {
        'newsObj': newsObj,
        'carouselNews':carouselNews,
        'eventsObj': eventsObj,
    }
    return render(request, 'main/main.html', context)


def newsPage(request):
    newsObj = News.objects.all().order_by('-date_created')
    
    context = {
        'newsObj': newsObj, 
    }
    return render(request, 'main/news-page.html', context)


def eventsPage(request):
    eventsObj = Events.objects.all().order_by('-date_created')

    context = {
        'eventsObj': eventsObj,
    }
    return render(request, 'main/events-page.html', context)


def aboutPage(request):
    brgyofficials = BrgyOfficials.objects.get(position='Barangay Captain')
    brgycouncilors = BrgyOfficials.objects.exclude(position='Barangay Captain')
    skofficials = SkOfficials.objects.get(position='SK Chairman')
    skkagawads = SkOfficials.objects.exclude(position='SK Chairman')

    context = {
        'brgyofficials':brgyofficials,
        'brgycouncilors': brgycouncilors,
        'skofficials': skofficials,
        'skkagawads': skkagawads,
    }
    return render(request, 'main/about-page.html', context)

def singleNewsPage(request, pk):
    newsObj = News.objects.get(id=pk)
    context = {
        'newsObj':newsObj
    }
    return render(request, 'main/single-news-page.html', context)


def singleEventPage(request, pk):
    eventsObj = Events.objects.get(id=pk)
    context = {
        'eventsObj':eventsObj
    }
    return render(request, 'main/single-event-page.html', context)


@login_required(login_url='login')
def createNews(request):
    profile = request.user.profiles
    form = NewsForm()

    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            news = form.save(commit=False)
            news.owner = profile
            news.save()
            return redirect('account')

    context = {
        'form':form,
    }
    return render(request, 'main/create-update-news.html', context)


@login_required(login_url='login')
def updateNews(request, pk):
    profile = request.user.profiles
    newsObj = profile.news_set.get(id=pk)
    form = NewsForm(instance=newsObj)

    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES, instance=newsObj)
        if form.is_valid():
            form.save()
            return redirect('account')

    context = {
        'form':form, 'newsObj': newsObj,
    }
    return render(request, 'main/create-update-news.html', context)


@login_required(login_url='login')
def deleteNews(request, pk):
    profile = request.user.profiles
    newsObj = profile.news_set.get(id=pk)

    if request.method == 'POST':
        newsObj.delete()
        return redirect('account')

    context = {
        'Obj': newsObj,
    }
    return render(request, 'main/delete-template.html', context)


@login_required(login_url='login')
def createEvents(request):
    profile = request.user.profiles
    form = EventsForm()

    if request.method == 'POST':
        form = EventsForm(request.POST, request.FILES)
        if form.is_valid():
            events = form.save(commit=False)
            events.owner = profile
            events.save()
            return redirect('account')

    context = {
        'form':form,
    }   
    return render(request, "main/create-update-events.html", context)


@login_required(login_url='login')
def updateEvents(request, pk):
    profile = request.user.profiles
    eventsObj = profile.events_set.get(id=pk)
    form = EventsForm(instance=eventsObj)

    if request.method == 'POST':
        form = EventsForm(request.POST, request.FILES, instance=eventsObj)
        if form.is_valid():
            form.save()
            return redirect('account')

    context = {
        'form':form
    }
    return render(request, 'main/create-update-events.html', context)


@login_required(login_url='login')
def deleteEvents(request, pk):
    profile = request.user.profiles
    eventsObj = profile.events_set.get(id=pk)

    if request.method == 'POST':
        eventsObj.delete()
        return redirect('account')
    
    context = {
        'Obj': eventsObj,
    }
    return render(request, 'main/delete-template.html', context)