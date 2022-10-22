from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerUser, name='register'),

    path('login-admin/', views.loginAdmin, name='login-admin'),

    path('profile/<str:pk>', views.userProfile, name='user-profile'),
    path('account/', views.userAccount, name='account'),
    path('edit-account/', views.editAccount, name='edit-account'),
    path('search-account/', views.searchAccount, name='search-account'),

    path('report-concern/d26b5cd8-0c06-4c7a-b1ac-030894b5e356', views.reportConcern, name='report-concern'),
    path('request-document/d26b5cd8-0c06-4c7a-b1ac-030894b5e356', views.requestDocument, name='request-document'),
    path('create-message/<str:pk>', views.createMessage, name='create-message'),

    path('inbox/', views.inbox, name='inbox'),
    path('request-message/<str:pk>', views.requestMessage, name='request-message'),
    path('report-message/<str:pk>', views.reportMessage, name='report-message'),
    path('view-message/<str:pk>', views.viewMessage, name='view-message'),
]