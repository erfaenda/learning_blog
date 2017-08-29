from django.shortcuts import render

# Create your views here.
def index(request):
    '''Домашняя страница приложения learning_blogs_app'''
    return render(request, 'learning_blog/index.html')
