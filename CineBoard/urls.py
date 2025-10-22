from django.urls import path
from . import views

app_name = 'CineBoard'

urlpatterns = [
    path('register/', views.RegisterCineView.as_view(), name='register_cine'),
    path('login/', views.LoginCineView.as_view(), name='login_cine'),
    path('logout/', views.LogoutCineView.as_view(), name='logout'),

    path('', views.FilmListView.as_view(), name='film_list'),
    path('film/<int:pk>/', views.FilmDetailView.as_view(), name='film_detail'),
    path('film/add/', views.FilmCreateView.as_view(), name='film_add'),
    path('film/<int:pk>/edit/', views.FilmUpdateView.as_view(), name='film_edit'),
    path('film/<int:pk>/delete/', views.FilmDeleteView.as_view(), name='film_delete'),

    path('search/', views.FilmSearchView.as_view(), name='film_search'),
    path('genre/<str:genre>/', views.FilmGenreView.as_view(), name='film_genre'),
    path('tag/<str:tag>/', views.FilmTagView.as_view(), name='film_tag'),
    path('control/', views.ControlView.as_view(), name='control'), 

    path('film/<int:pk>/comment/', views.AddCommentView.as_view(), name='add_comment'),
]
