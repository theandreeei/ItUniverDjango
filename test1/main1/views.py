from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('Hello, my name is Andrei')


def pet(request):
    return HttpResponse('I like dogs')


def about(request):
    return HttpResponse('<p1>Я Мордач Андрій Олегович<br>Я знаходжусь в Україні<br>Мені 14 повних років<br>Я вчусь у школі номер 23<br>Моє хобі це катання на велосипеді<br>Також я люблю вчитися, програмувати і займатися спортом</p1>')
