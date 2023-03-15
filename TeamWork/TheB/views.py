from django.shortcuts import render


def index(request):
    return render(request, 'TheB/index.html')


def about(request):
    return render(request, 'TheB/about.html')
