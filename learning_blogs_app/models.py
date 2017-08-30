from django.db import models

# Create your models here.
class Topic(models.Model):
    '''Класс характеризующий тему, темы нашего блога'''
    text = models.CharField(max_length=200) # Обычное текстовое поле, длина ограничена 200 символов
    date_added = models.DateTimeField(auto_now_add=True) # поле времени и даты с параметром добавлять сразу же
    def __str__(self):
        '''Возвращает строковое представление модели'''
        return self.text

class Chain(models.Model):
    '''основная информация хранящяяся в теме'''
    topic = models.ForeignKey(Topic) # связываем информацию с темой
    text = models.TextField() # текстовое поле без ограничений
    date_added = models.DateTimeField(auto_now_add=True) # время и дата когда добалена запись

    class Meta:
        verbose_name_plural = 'text message'

    def __str__(self):
        '''возвращает строковое представление модели'''
        if len(self.text) > 50:
            return self.text[:50] + '...' # возвращает только первые 50 символов от тема и добавляет многоточие
        else:return self.text # а если нет то просто возращает текст