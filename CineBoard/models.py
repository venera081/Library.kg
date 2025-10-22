from django.db import models
from django.contrib.auth.models import User
from django.db.models import Avg

class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Название тега')

    def __str__(self):
        return self.name

class Film(models.Model):
    GENRE_CHOICES = [
        ('Ужасы', 'Ужасы'),
        ('Фантастика', 'Фантастика'),
        ('Боевики', 'Боевики'),
        ('Мелодрама', 'Мелодрама'),
    ]

    title = models.CharField(max_length=100, verbose_name='Название фильма')
    description = models.TextField(verbose_name='Описание фильма')
    genre = models.CharField(max_length=50, choices=GENRE_CHOICES, default='Фантастика', verbose_name='Жанр')
    date = models.CharField(max_length=50, verbose_name='Дата выхода')
    tags = models.ManyToManyField(Tag, related_name='films', blank=True, verbose_name='Теги')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')

    def __str__(self):
        return self.title

    def average_rating(self):
        avg = self.reviews.aggregate(avg_mark=Avg('mark'))['avg_mark']
        return round(avg or 0, 1)

class Review(models.Model):
    film = models.ForeignKey(Film, on_delete=models.CASCADE, related_name='reviews')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    mark = models.IntegerField(default=5)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author} - {self.film}"
