from django.urls import path
from .views import index, dungion, minecraft, legends, earth, story_mode, story_mode_s2

urlpatterns = [
    path('', index, name='home'),
    path('home', index, name='index'),
    path('minecraft_dungion', dungion, name='dungion'),
    path('minecraft', minecraft, name='minecraft'),
    path('legends', legends, name='legends'),
    path('earth', earth, name='earth'),
    path('story', story_mode, name='story'),
    path('storys2', story_mode_s2, name='storys2'),
]