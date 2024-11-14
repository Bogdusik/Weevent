from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('account/', views.account, name='account'),
    path('faq/', views.faq, name='faq'),
    path('favourites/', views.favourites, name='favourites'),
    path('llama/', views.llama, name='llama'),
    path('map/', views.map, name='map'),
    path('preferences/', views.preferences, name='preferences'),
    path('events/', views.events, name='events'),
    

]