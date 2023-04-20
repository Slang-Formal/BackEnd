from django.urls import path
from . import views


urlpatterns = [
    path('', views.say_hello), 
    path('slangreturn/', views.slangreturn, name = 'slang-response'),
    path('test', views.submit_string, name='submit_string'),
]
