from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import Avg


class Books(models.Model):
    title = models.CharField(max_length=100, verbose_name='напишите название книги')
    description = models.TextField(verbose_name='укажите описание книги')
    image = models.ImageField(upload_to='books/', verbose_name='загрузите картинку книги')
    quatity_page = models.PositiveIntegerField(verbose_name='укажите кол-во страниц', blank=True)
    author = models.CharField(max_length=100, blank=True, verbose_name='укажите автора книги')
    book_audio = models.URLField(verbose_name='укажите ссылку с youtube')
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def average_rating(self):
        avg = self.reviews.aggregate(avg_mark=Avg('mark'))['avg_mark']
        return avg or 0


    def __str__(self):
        return self.title


    class Meta:
         verbose_name = 'книга'
         verbose_name_plural = 'книги'


class Reviews(models.Model):
    choice_book = models.ForeignKey(Books, on_delete=models.CASCADE, related_name="reviews")
    mark = models.PositiveIntegerField(verbose_name='поставьте оценку от 1 до 5', 
                                       validators=[MaxValueValidator(5), MinValueValidator(1)])
    review_text = models.TextField(blank=True, default='Классная книга')  
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.choice_book} - {self.mark}'


    class Meta:
        verbose_name = 'отзыв'
        verbose_name_plural = 'отзывы'






class Person(models.Model):
    name = models.CharField(max_length=100, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'участника'
        verbose_name_plural = 'участники'

class Tournament(models.Model):
    passport = models.OneToOneField(Person, on_delete=models.CASCADE, related_name='participant')
    choice_tournament = models.CharField(max_length=100, default='Конный тур')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.passport.name}: {self.choice_tournament}'
    
    class Meta:
        verbose_name = 'тур'
        verbose_name_plural = 'туры'
    



