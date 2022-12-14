from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerUser, name='register'),

    path('login-admin/', views.loginAdmin, name='login-admin'),

    path('profile/<str:pk>', views.userProfile, name='user-profile'),
    path('profile-walkin/<str:pk>', views.userProfileWalkIn, name='user-profile-walkin'),
    path('account/', views.userAccount, name='account'),
    path('edit-account/', views.editAccount, name='edit-account'),
    path('search-account/', views.searchAccount, name='search-account'),

    path('report-concern/d26b5cd8-0c06-4c7a-b1ac-030894b5e356', views.reportConcern, name='report-concern'),
    path('request-document/d26b5cd8-0c06-4c7a-b1ac-030894b5e356', views.requestDocument, name='request-document'),
    path('request-document-walkin/', views.walkinRequestDocument, name='request-document-walkin'),
    path('verification/d26b5cd8-0c06-4c7a-b1ac-030894b5e356', views.verifyAccount, name='verify-account'),
    path('create-message/<str:pk>', views.createMessage, name='create-message'),
    path('send-message/<str:pk>', views.createSendMessage, name='send-message'),

    path('inbox/', views.inbox, name='inbox'),
    path('request-message/<str:pk>', views.requestMessage, name='request-message'),
    path('report-message/<str:pk>', views.reportMessage, name='report-message'),
    path('remark-message/<str:pk>', views.remarkReports, name='remark-message'),
    path('verify-message/<str:pk>', views.verifyMessage, name='verify-message'),
    path('view-message/<str:pk>', views.viewMessage, name='view-message'),
    path('view-walkin-message/<str:pk>', views.viewWalkinMessage, name='view-walkin-message'),
    path('send-view-message/<str:pk>', views.sendViewMessage, name='send-view-message'),
    path('single-request-message/<str:pk>', views.singleRequestMessage, name='single-request-message'),
    path('single-report-message/<str:pk>', views.singleReportMessage, name='single-report-message'),

    path('verified/<str:pk>', views.verified, name='verified'),

    path('history/', views.history, name='history'),
    path('single-history/<str:pk>', views.singleHistory, name='single-history'),

    path('export-data-requests/', views.export_data_requests, name='export-data-requests'),
    path('export-data-requests-walkin/', views.export_data_walkinrequests, name='export-data-requests-walkin'),
    path('export-data-reports/', views.export_data_reports, name='export-data-reports'),

    path('delete-request/<str:pk>', views.deleteRequest, name='delete-request'),
    path('delete-request-walkin/<str:pk>', views.deleteWalkinRequest, name='delete-request-walkin'),
    path('delete-report/<str:pk>', views.deleteReport, name='delete-report'),
    path('delete-verification/<str:pk>', views.deleteVerification, name='delete-ver'),
    path('done-request/<str:pk>', views.doneRequest, name='done-request'),
    path('done-report/<str:pk>', views.doneReport, name='done-report'),
    path('done-ver/<str:pk>', views.doneVerification, name='done-ver'),

    path('create-profile/', views.createProfile, name='create-profile')
]