from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('books/', include('books.urls')),
    path('basket/', include('basket.urls')),
    path('users/', include('users.urls')),  
    path('captcha/', include('captcha.urls')),
    path('clothes/', include('clothes.urls')),

    path('cine/', include('CineBoard.urls')),  
]
