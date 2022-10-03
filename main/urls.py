from django.urls import path
from . import views

urlpatterns = [
    path('', views.mainPage, name='main-page'),
    path('news-page/', views.newsPage, name='news-page'),
    path('events-page/', views.eventsPage, name='events-page'),
    path('about-page/', views.aboutPage, name='about-page'),

    path('single-news/<str:pk>', views.singleNewsPage, name='single-news'),
    path('single-event/<str:pk>', views.singleEventPage, name='single-event'),

    path('create-news/', views.createNews, name='create-news'),
    path('update-news/<str:pk>', views.updateNews, name='update-news'),
    path('delete-news/<str:pk>', views.deleteNews, name='delete-news'),

    path('create-events/', views.createEvents, name='create-events'),
    path('update-events/<str:pk>', views.updateEvents, name='update-events'),
    path('delete-events/<str:pk>', views.deleteEvents, name='delete-events'),
]

