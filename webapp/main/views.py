from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm




def index(request):
    if request.method == "POST":
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            error = 'Заявка успешно принята!'
        else:
            error = 'Неверно заполнена форма'
    form = ArticlesForm()
    error = ''
    data = {'form': form,
            'error': error}



    return render(request, 'main/index.html', data)


def about(request):
    return render(request, 'main/about.html')
