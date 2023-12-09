from django.shortcuts import render

def mainPage(request):
    return render(request, 'mainPage.html')

def aboutUs(request):
    return render(request, 'aboutUs.html')