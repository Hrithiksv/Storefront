from django.shortcuts import render
from django.http import HttpResponse
from .models import Topics

# Create your views here.
# request-> response
# request handler


def say_hello(request):
    return render(request, 'hello.html', {'name': 'Hrithik'})


def topics(request):
    topics = Topics.objects.order_by('Date')
    context = {'topics': topics}
    return render(request, 'topics.html', context)
