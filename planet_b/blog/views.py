from django.shortcuts import render


def home(request):
    return render(request, "blog/index.html")


def register(request):
    return render(request, "blog/register.html")

