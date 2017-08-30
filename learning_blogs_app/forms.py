from django import forms # импортируем формы
from .models import Topic # импортируем модель с которой хотим работать

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic # Форма создается на базе модели Topic
        fields = ['text'] #  а на ней размещается поле текст
        labels = {'text': ''} # приказываем не генерировать подпись для текстового поля