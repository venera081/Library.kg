from django.urls import path
from . import views

urlpatterns = [
    path('all_clothes/', views.AllClothesView.as_view(), name='all_clothes'),
    path('women_clothes/', views.WomenClothesView.as_view(), name='women_clothes'),
    path('men_clothes/', views.MenClothesView.as_view(), name='men_clothes'),
    path('kids_clothes/', views.KidsClothesView.as_view(), name='kids_clothes'),
    path('search/', views.SearchView.as_view(), name='search'),
]