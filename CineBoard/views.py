from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from .models import Film, Review
from .forms import FilmForm, ReviewForm
from django.db.models import Avg
from django.views import generic



class RegisterCineView(generic.FormView):
    template_name = 'CineBoard/register_cine.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('CineBoard:login_cine') 

    def form_valid(self, form):
        form.save()  
        return super().form_valid(form)



class LoginCineView(generic.FormView):
    template_name = 'CineBoard/login_cine.html'
    form_class = AuthenticationForm
    success_url = reverse_lazy('CineBoard:film_list')

    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()
        return form_class(self.request, **self.get_form_kwargs())

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super().form_valid(form)



class LogoutCineView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('CineBoard:register_cine')


class FilmListView(ListView):
    model = Film
    template_name = 'CineBoard/film_list.html'
    context_object_name = 'films'

    def get_queryset(self):
        return Film.objects.annotate(avg_rating=Avg('reviews__mark')).order_by('-avg_rating', '-created_at')
    
class ControlView(ListView):
    model = Film
    template_name = 'CineBoard/control.html'
    context_object_name = 'films'

    def get_queryset(self):
        return Film.objects.annotate(avg_rating=Avg('reviews__mark')).order_by('-avg_rating', '-created_at')


class FilmDetailView(DetailView):
    model = Film
    template_name = 'CineBoard/film_detail.html'
    context_object_name = 'film'

class FilmCreateView(CreateView):
    model = Film
    form_class = FilmForm
    template_name = 'CineBoard/film_form.html'
    success_url = reverse_lazy('CineBoard:film_list')

class FilmUpdateView(UpdateView):
    model = Film
    form_class = FilmForm
    template_name = 'CineBoard/film_form.html'
    success_url = reverse_lazy('CineBoard:film_list')

class FilmDeleteView(DeleteView):
    model = Film
    template_name = 'CineBoard/film_confirm_delete.html'
    success_url = reverse_lazy('CineBoard:film_list')


class FilmSearchView(ListView):
    model = Film
    template_name = 'CineBoard/film_list.html'
    context_object_name = 'films'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Film.objects.filter(title__icontains=query) if query else Film.objects.all()

class FilmGenreView(ListView):
    model = Film
    template_name = 'CineBoard/film_list.html'
    context_object_name = 'films'

    def get_queryset(self):
        genre = self.kwargs['genre']
        return Film.objects.filter(genre=genre)
    
class FilmTagView(ListView):
    model = Film
    template_name = 'CineBoard/film_list.html'
    context_object_name = 'films'

    def get_queryset(self):
        tag_name = self.kwargs['tag']
        return Film.objects.filter(tags__name=tag_name).annotate(avg_rating=Avg('reviews__mark')).order_by('-avg_rating')


class AddCommentView(View):
    def post(self, request, pk):
        film = get_object_or_404(Film, pk=pk)
        if request.user.is_authenticated:
            text = request.POST.get('text')  # берем только текст комментария
            if text:
                Review.objects.create(
                    film=film,
                    author=request.user,
                    text=text
                )
        return redirect('CineBoard:film_detail', pk=pk)

    def get(self, request, pk):
        return redirect('CineBoard:film_detail', pk=pk)
