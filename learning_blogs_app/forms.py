from django import forms # импортируем формы
from .models import Topic, Chain # импортируем модель с которой хотим работать

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic # Форма создается на базе модели Topic
        fields = ['text'] #  а на ней размещается поле текст
        labels = {'text': ''} # приказываем не генерировать подпись для текстового поля

class ZapisForm(forms.ModelForm):
    class Meta:
        model = Chain
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})} #переопределяет виджет, поле ввода текста 80 строк шириной
