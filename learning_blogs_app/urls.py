'''Определяет схемы URL для learning_blogs_app'''

from django.conf.urls import url # импорт функции необходимый для работы с URL
from . import views # импортируем представляения views из этой папки

urlpatterns = [ # список страниц которые могут запрашиваться из lerning_blogs_app
    # Домашняя страница
    url(r'^$', views.index, name='index'),
    # все что после r идет без дополнительной обработки ^ - начало строки, $ - конец строки, т.е пустой адресс
    # когда адрес совпадает с регулярным выражением будет вызвана функция views.index
    # index - имя на которое можно ссылаться для доступа к этой схеме
        # Отображение всех тем, видимо будет главной страницей
        url(r'^topics/$', views.topics, name='topics'),
            #Страница с подробностями по изученной теме
            url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'), #тут ничего не ясно
        # страница для добавления новой темы
        url(r'^new_topic/$', views.new_topic, name='new_topic'),
        # страница для длбавления новой записи
        url(r'^new_zapis/(?P<topic_id>\d+)/$', views.new_zapis, name='new_zapis'),


]