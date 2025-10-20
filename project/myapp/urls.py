from django.urls import path
from .views import index, dungion, minecraft

urlpatterns = [
    path('home', index, name='index'),
    path('minecraft_dungion', dungion, name='dungion'),
    path('minecraft', minecraft, name='minecraft'),
]