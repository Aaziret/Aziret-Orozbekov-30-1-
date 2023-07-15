from django.shortcuts import HttpResponse


def hello(requests):
    if requests.method == 'GET':
        return HttpResponse('Hello! Its my project')


def now_date(requests):
    if requests.method == 'GET':
        return HttpResponse('15.07.2023')


def goodbye(requests):
    if requests.method == 'GET':
        return HttpResponse('Goodbye user!')
