from django.shortcuts import render
from .models import Topic # имортируем связанную с нужными нам данными - Topics

# Create your views here.
def index(request):
    '''Домашняя страница приложения learning_blogs_app'''
    return render(request, 'learning_blog/index.html')

def topics(request):
    '''Страница с выбором списков тем'''
    topics = Topic.objects.order_by('date_added') # запрос к базе данных объектов Topic отсвортированный по дате добавления
    context = {'topics': topics}
    return render(request, 'learning_blog/topics.html', context)
