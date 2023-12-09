from django.urls import path, include
from .views import *

urlpatterns = [
    path('account/', include('authentication.urls')),
    path('api/v1/', include('api.urls')),
    path('trainings/', include('exercise_manager.urls')),
    path('home/', mainPage, name='mainPage'),
    path('aboutUs/', aboutUs, name='aboutUs'),
]