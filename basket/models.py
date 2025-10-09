from django.db import models
from books.models import Books

class Basket(models.Model):
    choice_book = models.ForeignKey(Books, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name='Какую книгу вы хотите заказать?')
    description_book = models.TextField('Введите описание книги')
    phone = models.CharField(max_length=100, verbose_name='Укажите ваш номер телефона')
    address = models.CharField(max_length=100, verbose_name='Введите наш адрес доставки вашего города')

    






