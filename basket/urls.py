from django.urls import path
from . import views

urlpatterns = [
    path('basket_list/', views.readBasket, name='basket_list'),
    path('basket_list/<int:id>/update/', views.updateBasket, name='update_basket'),
     path('basket_list/<int:id>/delete/', views.deleteBasket, name='delete_basket'),


    path('create_basket/', views.createBasket, name='create_basket'),
]