from django.urls import path
from . import views

app_name = 'playground'
# URLConf
urlpatterns = [
    path('home/', views.say_hello, name='home'),
    path('topic/', views.topics, name='topic'),
]
