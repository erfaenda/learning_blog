from django.shortcuts import render
from .models import Topic # имортируем связанную с нужными нам данными - Topics
from .forms import TopicForm, ZapisForm
from django.http import HttpResponseRedirect # для перенаправления пользователя к странице топикс
from django.core.urlresolvers import reverse # тоже какая то хуйня для редерикта

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

def new_topic(request):
    '''Определяет новую тему.'''
    if request.method != 'POST': # если метод запроса не ПОСТ отправим пустую форму
        # данные не отправились; создается пустая форма.
        form = TopicForm() # создаем экземпляр Топик ФОрм, он передается в контекст
    else:
        # Отправлены данные POST; обработаные данные.
        form = TopicForm(request.POST)
        if form.is_valid(): # нельзя записать данные пока они не будут проверены
            form.save() # если верные то сохраняем
            return HttpResponseRedirect(reverse('learning_blogs_app:topics')) # переадресовывает нас обратно в список тем

    context = {'form': form}
    return render(request, 'learning_blog/new_topic.html', context)

def new_zapis(request, topic_id):
    '''Добавляет новую запись по конкретной теме'''
    topic = Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        form = ZapisForm()
    else:
        form = ZapisForm(data=request.POST)
        if form.is_valid():
            new_zapis = form.save(commit=False)
            new_zapis.topic = topic
            new_zapis.save()
            return HttpResponseRedirect(reverse('learning_blogs_app:topic', args=[topic_id]))

    context = {'topic': topic, 'form': form}
    return render(request, 'learning_blog/new_zapis.html', context)