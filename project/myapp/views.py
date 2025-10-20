from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def dungion(request):
    return render(request, 'dungion.html')

def minecraft(request):
    return render(request, 'minecraft.html')
