from django.shortcuts import render, HttpResponse


def front(request):
    return render(request, "front.html")