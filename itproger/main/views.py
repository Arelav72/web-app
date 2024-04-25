from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("<h4>Проверка страницы.</h4>")

def about(request):
    return HttpResponse("<h4>О нас.</h4>")

def contact(request):
    return HttpResponse("<h4>Контакты.</h4>")

def services(request):
    return HttpResponse("<h4>Услуги.</h4>")

def portfolio(request):
    return HttpResponse("<h4>Портфолио.</h4>")

def blog(request):
    return HttpResponse("<h4>Блог.</h4>")

