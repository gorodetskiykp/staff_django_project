from django.shortcuts import render
from django.http import HttpResponse

from .models import Item


def hello(request):
    return HttpResponse("Hello")


def menu(request):
    template = "staff/index.html"
    context = {}
    return render(request=request, template_name=template, context=context)


def staff_list(request):
    # собрать данные из модели
    items = Item.objects.all()  # list[Item] - QuerySet
    # подключить html-шаблон
    template = "staff/staff_list.html"
    # создаем контекст - переменные шаблона
    context = {
        "t_title": "Список вещей",
        "t_items": items,
    }
    return render(request=request, template_name=template, context=context)
