from django.http import HttpResponse
from django.shortcuts import render

from core.models import Jewelry


def home(request):
    return render(request, 'core/base.html', dict(title='home', content='<h1>Добро пожаловать<h1>'))


def table(request):
    jews = Jewelry.objects.all()
    return render(request, 'core/table.html', dict(title='table', table_name='Каталог украшений', jews=jews))


def jewelry(request, pk):
    jew = Jewelry.objects.get(pk=pk)
    return render(request, 'core/jewelry.html', dict(title='jewelry', jew=jew))
