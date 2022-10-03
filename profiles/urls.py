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

    path('report-concern/', views.reportConcern, name='report-concern'),
]