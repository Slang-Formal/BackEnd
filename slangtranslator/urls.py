from django.urls import path
from . import views


urlpatterns = [
    path('hello/', views.say_hello), 
    path('slangreturn/', views.slangreturn, name = 'slang-response'),
    path('', views.submit_string, name='submit_string'),
]
