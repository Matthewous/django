from django.http import HttpResponse
from django.shortcuts import render, reverse
import datetime
from os import listdir

def home_view(request):
    template_name = 'app/home.html'

    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }
    
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):

    current_time = datetime.datetime.now().time()
    msg = f'Текущее время: {current_time}'
    return HttpResponse(msg)


def workdir_view(request):
    
    content = listdir('/Users/matthew/Documents/GitHub/django/first_project')
    return render(request, '/Users/matthew/Documents/GitHub/django/first_project/app/templates/app/workdir.html', {'content_list': content})
