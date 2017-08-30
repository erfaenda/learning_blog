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

def topic(request, topic_id): # функция получает значение совпадающее с (?P<topic_id>\d+) и сохраняет его в topic_id
    '''выводит одну тему и все ее записи'''
    topic = Topic.objects.get(id=topic_id) # получаем тему
    chains = topic.chain_set.order_by('-date_added') # получаем все записи связанные с темой, они упорядочиваются по дате знак "-" означает что это в обратном порядке
    context = {'topic': topic, 'chains': chains} # полученные,темы и записи сохраняем в словарь
    return render(request, 'learning_blog/topic.html', context) # и передаем из шаблону
