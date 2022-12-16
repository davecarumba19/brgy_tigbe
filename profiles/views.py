from django.shortcuts import render, redirect

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from django.db.models import Q

from django.contrib import messages
from .models import Profiles, Requests, Reports, Verificationss, WalkInProfiles, WalkInRequests
from main.models import News, Events
from .forms import CustomUserCreationForm, ProfileForm, ReportsForm, RemarkReportsForm, RequestsForm, MessageForm, SendMessageForm, VerificationForm, VerifyProfileForm, WalkInProfileForm, WalkInRequestsForm

from .resources import RequestResource, ReportResource, WalkInRequestResource
from django.http import HttpResponse
from tablib import Dataset

from django.template.loader import get_template
from xhtml2pdf import pisa

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
        form = CustomUserCreationForm(request.POST, request.FILES)

        phone_number = request.POST['phone_number']
        blk_unit = request.POST['blk_unit']
        phase_street = request.POST['phase_street']
        status = request.POST['status']
        gender = request.POST['gender']
        vaccine = request.POST['vaccine']
        village = request.POST['village']
        profile_image = request.FILES['profile_image']

        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.phone_number = phone_number
            user.blk_unit = blk_unit
            user.phase_street = phase_street
            user.status = status
            user.gender = gender
            user.vaccine = vaccine
            user.village = village
            user.profile_image = profile_image
            user.save()

            messages.success(request, 'User has been created!')
            messages.success(request, 'Verify your Profile to Access Request Document and Report Concerns feature!')
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
def userProfileWalkIn(request, pk):
    walkInProfiles = WalkInProfiles.objects.get(id=pk)

    context = {
        'walkInProfiles':walkInProfiles,
    }
    return render(request, 'profiles/walkin-profiles.html', context)

@login_required(login_url='login')
def userAccount(request):
    profile = request.user.profiles
    newsObj = News.objects.all().order_by('-date_created')
    eventsObj = Events.objects.all().order_by('-date_created')[:3]
    walkinprofile = WalkInProfiles.objects.all().count()

    context = {
        'profile': profile,
        'newsObj': newsObj,
        'eventsObj': eventsObj,
        'walkinprofile': walkinprofile,
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
    
    profiles = Profiles.objects.filter(
        Q(first_name__icontains=search_account) |
        Q(id__icontains=search_account) |
        Q(village__icontains=search_account)
        )

    profile1 = Profiles.objects.filter(village__icontains=search_account, verified=True).count()
    profile2 = WalkInProfiles.objects.filter(village__icontains=search_account).count()
    
    totalProfile = profile1 + profile2

    walkInProfiles = WalkInProfiles.objects.filter(
        Q(first_name__icontains=search_account) |
        Q(id__icontains=search_account) |
        Q(village__icontains=search_account)
        )

    context = {
        'profiles':profiles,
        'walkInProfiles':walkInProfiles,
        'totalProfile':totalProfile,
        'search_account':search_account,
    }
    return render(request, 'profiles/search-account.html', context)



def loginAdmin(request):

    if request.user.is_authenticated:
        return redirect('account')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = User.objects.filter(username='admin')
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
    verifySendMessage = profile.send_message.all()
    verifyMessage = profile.verification.all()
    unreadCountDocument = requestDocument.filter(is_read=False).count()
    unreadCountReport = reportConcern.filter(is_read=False).count()
    unreadMessage = sendMessage.filter(is_read=False).count()
    unreadVerifySendMessage = verifySendMessage.filter(is_read=False).count()
    unreadVerification = verifyMessage.filter(is_read=False).count()
    walkinprofile = WalkInProfiles.objects.all().count()

    context = {
        'requestDocument': requestDocument,
        'reportConcern': reportConcern,
        'sendMessage': sendMessage,
        'verifyMessage': verifyMessage,
        'verifySendMessage': verifySendMessage,
        'unreadCountDocument': unreadCountDocument,
        'unreadCountReport': unreadCountReport,
        'unreadMessage': unreadMessage,
        'unreadVerifySendMessage': unreadVerifySendMessage,
        'unreadVerification': unreadVerification,
        'profile': profile,
        'walkinprofile': walkinprofile,
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
def singleRequestMessage(request, pk):
    requestMessage = Requests.objects.get(id=pk)

    context = {
        'requestMessage':requestMessage
    }
    return render(request, 'profiles/single-request-message.html', context)



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
def singleReportMessage(request, pk):
    reportMessage = Reports.objects.get(id=pk)

    context = {
        'reportMessage':reportMessage
    }
    return render(request, 'profiles/single-reports-message.html', context)



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
            report.sender_username = profile.first_name
            report.receiver_username = receiver.username

            report.save()
            return redirect('account')

    context = {
        'form':form,
    }
    return render(request, 'profiles/reports.html', context)


@login_required(login_url='login')
def remarkReports(request, pk):
    profile = request.user.profiles
    remarkObj = Reports.objects.get(id=pk)
    form = RemarkReportsForm()

    if request.method == 'POST':
        form = RemarkReportsForm(request.POST, instance=remarkObj)
        if form.is_valid():
            report = form.save(commit=False)

            report.save()
            return redirect('account')

    context = {
        'form':form,
    }
    return render(request, 'profiles/remark-report.html', context)


@login_required(login_url='login')
def requestDocument(request):
    page = 'reqdoc'
    profile = request.user.profiles
    receiver = Profiles.objects.get(id='d26b5cd8-0c06-4c7a-b1ac-030894b5e356')
    form = RequestsForm()

    if request.method == 'POST':
        form = RequestsForm(request.POST)
        if form.is_valid():
            request = form.save(commit=False)
            request.sender = profile
            request.receiver = receiver
            request.sender_username = profile.first_name
            request.receiver_username = receiver.username

            request.save()
            return redirect('account')

    context = {
        'form':form,
        'page':page,
    }
    return render(request, 'profiles/request.html', context)



@login_required(login_url='login')
def walkinRequestDocument(request):
    page = 'walkinreq'
    profile = request.user.profiles
    form = WalkInRequestsForm()

    if request.method == 'POST':
        form = WalkInRequestsForm(request.POST)
        if form.is_valid():
            request = form.save(commit=False)
        
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
            user = form.save(commit=False)
            user.verified = True
            user.save()

            return redirect('account')

    context = {
        'form':form,
        'profile':profile,
    }
    return render(request, 'profiles/verified.html', context)



@login_required(login_url='login')
def createMessage(request, pk):
    page = 'createmessage'

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
        'page': page,
    }
    return render(request, 'profiles/create-message.html', context)


@login_required(login_url='login')
def createSendMessage(request, pk):
    page = 'createsendmessage'

    profile = request.user.profiles
    receiver = Profiles.objects.get(id=pk)
    form = SendMessageForm()

    if request.method == 'POST':
        form = SendMessageForm(request.POST, request.FILES)
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
    
    template_path = 'profiles/view-message.html'
    context = {'sendMessage': sendMessage}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="document.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funny view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


@login_required(login_url='login')
def viewWalkinMessage(request, pk):
    profile = request.user.profiles
    sendMessage = WalkInRequests.objects.get(id=pk)

    if sendMessage.is_read == False:
        sendMessage.is_read = True
        sendMessage.save()
    
    template_path = 'profiles/view-walkin-message.html'
    context = {'sendMessage': sendMessage}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="document.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funny view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


@login_required(login_url='login')
def sendViewMessage(request, pk):
    profile = request.user.profiles
    sendViewMessage = profile.send_message.get(id=pk)

    if sendViewMessage.is_read == False:
        sendViewMessage.is_read = True
        sendViewMessage.save()

    context = {
        'sendViewMessage':sendViewMessage,
    }
    return render(request, 'profiles/sendView-message.html', context)



@login_required(login_url='login')
def history(request):
    search_request_report = ''

    profile = request.user.profiles
    historyVerifications = Verificationss.objects.all().order_by('-date_created')
    totalRequest = Requests.objects.filter(hide=False).count()
    totalWalkinRequest = WalkInRequests.objects.filter(hide=False).count()
    totalReports = Reports.objects.filter(hide=False).count()
    totalVerifications = Verificationss.objects.all().count()
    singleHistoryRequest = Requests.objects.filter(sender=profile.id).order_by('-date_created')
    singleHistoryReports = Reports.objects.filter(sender=profile.id).order_by('-date_created')
    singleTotalRequest = Requests.objects.filter(sender=profile.id).count()
    singleTotalReports = Reports.objects.filter(sender=profile.id).count()
    walkinprofile = WalkInProfiles.objects.all().count()



    if request.GET.get('searchRequestReport'):
        search_request_report = request.GET.get('searchRequestReport')

    historyRequest = Requests.objects.filter(
        Q(sender__first_name__icontains=search_request_report) |
        Q(sender__last_name__icontains=search_request_report) |
        Q(purpose__icontains=search_request_report) |
        Q(document_type__icontains=search_request_report) |
        Q(date_created__icontains=search_request_report)
        ).order_by('-date_created')
        
    historyWalkinRequest = WalkInRequests.objects.filter(
        Q(owner__first_name__icontains=search_request_report) |
        Q(owner__last_name__icontains=search_request_report) |
        Q(purpose__icontains=search_request_report) |
        Q(document_type__icontains=search_request_report) |
        Q(date_created__icontains=search_request_report)
        ).order_by('-date_created')

    historyReports = Reports.objects.filter(
        Q(sender__first_name__icontains=search_request_report) |
        Q(sender__last_name__icontains=search_request_report) |
        Q(date_created__icontains=search_request_report)
        ).order_by('-date_created')

    context = {
        'profile':profile,
        'historyRequest': historyRequest,
        'historyReports': historyReports,
        'historyWalkinRequest': historyWalkinRequest,
        'historyVerifications': historyVerifications,
        'totalRequest': totalRequest,
        'totalWalkinRequest': totalWalkinRequest,
        'totalReports': totalReports,
        'totalVerifications': totalVerifications,
        'singleHistoryRequest': singleHistoryRequest,
        'singleHistoryReports': singleHistoryReports,
        'singleTotalRequest': singleTotalRequest,
        'singleTotalReports': singleTotalReports,
        'walkinprofile': walkinprofile,
    }
    return render(request, 'profiles/history.html', context)


@login_required(login_url='login')
def singleHistory(request, pk):
    profile = Profiles.objects.get(id=pk)
    singleHistoryRequest = Requests.objects.filter(sender=pk).order_by('-date_created')
    singleHistoryReports = Reports.objects.filter(sender=pk).order_by('-date_created')
    singleTotalRequest = Requests.objects.filter(sender=pk).count()
    singleTotalReports = Reports.objects.filter(sender=pk).count()

    context = {
        'profile': profile,
        'singleHistoryRequest': singleHistoryRequest,
        'singleHistoryReports': singleHistoryReports,
        'singleTotalRequest': singleTotalRequest,
        'singleTotalReports': singleTotalReports,
    }
    return render(request, 'profiles/single-history.html', context)


@login_required(login_url='login')
def export_data_requests(request):
    hide = Requests.objects.filter(hide=False)
    if request.method == 'POST':
        # Get selected option from form
        file_format = request.POST['file-format']
        request_resource = RequestResource()
        dataset = request_resource.export(hide)
        if file_format == 'CSV':
            response = HttpResponse(dataset.csv, content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="requests_exported_data.csv"'
            return response        
        elif file_format == 'JSON':
            response = HttpResponse(dataset.json, content_type='application/json')
            response['Content-Disposition'] = 'attachment; filename="exported_data.json"'
            return response
        elif file_format == 'XLS (Excel)':
            response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
            response['Content-Disposition'] = 'attachment; filename="exported_data.xls"'
            return response   

    return render(request, 'profiles/export.html')



@login_required(login_url='login')
def export_data_walkinrequests(request):
    hide = WalkInRequests.objects.filter(hide=False)
    if request.method == 'POST':
        # Get selected option from form
        file_format = request.POST['file-format']
        request_resource = WalkInRequestResource()
        dataset = request_resource.export(hide)
        if file_format == 'CSV':
            response = HttpResponse(dataset.csv, content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="walkin_requests_exported_data.csv"'
            return response        
        elif file_format == 'JSON':
            response = HttpResponse(dataset.json, content_type='application/json')
            response['Content-Disposition'] = 'attachment; filename="exported_data.json"'
            return response
        elif file_format == 'XLS (Excel)':
            response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
            response['Content-Disposition'] = 'attachment; filename="exported_data.xls"'
            return response   

    return render(request, 'profiles/export.html')


@login_required(login_url='login')
def export_data_reports(request):
    hide = Reports.objects.filter(hide=False)
    if request.method == 'POST':
        # Get selected option from form
        file_format = request.POST['file-format']
        report_resource = ReportResource()
        dataset = report_resource.export(hide)
        if file_format == 'CSV':
            response = HttpResponse(dataset.csv, content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="reports_exported_data.csv"'
            return response        
        elif file_format == 'JSON':
            response = HttpResponse(dataset.json, content_type='application/json')
            response['Content-Disposition'] = 'attachment; filename="exported_data.json"'
            return response
        elif file_format == 'XLS (Excel)':
            response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
            response['Content-Disposition'] = 'attachment; filename="exported_data.xls"'
            return response   

    return render(request, 'profiles/export.html')


@login_required(login_url='login')
def deleteRequest(request, pk):
    requestObj = Requests.objects.get(id=pk)

    if request.method == 'POST':
        requestObj.hide = True
        requestObj.save()
        return redirect('account')

    context = {
        'Obj': requestObj,
    }
    return render(request, 'profiles/delete-template.html', context)


@login_required(login_url='login')
def deleteWalkinRequest(request, pk):
    requestObj = WalkInRequests.objects.get(id=pk)

    if request.method == 'POST':
        requestObj.hide = True
        requestObj.save()
        return redirect('account')

    context = {
        'Obj': requestObj,
    }
    return render(request, 'profiles/delete-template.html', context)


@login_required(login_url='login')
def doneRequest(request, pk):
    requestObj = Requests.objects.get(id=pk)

    if request.method == 'POST':
        requestObj.done = True
        requestObj.save()
        return redirect('account')

    context = {
        'Obj': requestObj,
    }
    return render(request, 'profiles/done-template.html', context)


@login_required(login_url='login')
def deleteReport(request, pk):
    reportObj = Reports.objects.get(id=pk)

    if request.method == 'POST':
        reportObj.hide = True
        reportObj.save()
        return redirect('account')

    context = {
        'Obj': reportObj,
    }
    return render(request, 'profiles/delete-template.html', context)


@login_required(login_url='login')
def deleteVerification(request, pk):
    verObj = Verificationss.objects.get(id=pk)

    if request.method == 'POST':
        verObj.hide = True
        verObj.done = True
        verObj.save()
        return redirect('account')

    context = {
        'Obj': verObj,
    }
    return render(request, 'profiles/ver-template.html', context)


@login_required(login_url='login')
def doneReport(request, pk):
    reportObj = Reports.objects.get(id=pk)

    if request.method == 'POST':
        reportObj.done = True
        reportObj.save()
        return redirect('account')

    context = {
        'Obj': reportObj,
    }
    return render(request, 'profiles/done-template.html', context)

@login_required(login_url='login')
def doneVerification(request, pk):
    verObj = Verificationss.objects.get(id=pk)

    if request.method == 'POST':
        verObj.done = True
        verObj.save()
        return redirect('account')

    context = {
        'Obj': verObj,
    }
    return render(request, 'profiles/done-template.html', context)

@login_required(login_url='login')
def createProfile(request):
    profile = request.user.profiles
    form = WalkInProfileForm()

    if request.method == 'POST':
        form = WalkInProfileForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.created_by = profile
            user.save()
            return redirect('account')

    context = {
        'form':form,
    }
    return render(request, 'profiles/create-profile.html', context)