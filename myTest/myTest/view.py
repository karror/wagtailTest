from django.shortcuts import render


def index(request):
    return render(request, "public/index.html")


def details(request):
    return render(request, "public/details/index.html")
