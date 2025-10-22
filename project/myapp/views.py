from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def dungion(request):
    return render(request, 'dungion.html')

def minecraft(request):
    return render(request, 'minecraft.html')

def legends(request):
    return render(request, 'legends.html')

def earth(request):
    return render(request, 'minecraft_earth.html')

def story_mode(request):
    return render(request, 'minecraft_story_mode.html')

def story_mode_s2(request):
    return render(request, 'minecraft_story_mode_s2.html')
