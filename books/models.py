from django.db import models

class Books(models.Model):
    title = models.CharField(max_length=100, verbose_name='напишите название книги')
    description = models.TextField(verbose_name='укажите описание книги')
    image = models.ImageField(upload_to='books/', verbose_name='загрузите картинку книги')
    quatity_page = models.PositiveIntegerField(verbose_name='укажите кол-во страниц', blank=True)
    author = models.CharField(max_length=100, blank=True, verbose_name='укажите автора книги')
    book_audio = models.URLField(verbose_name='укажите ссылку с youtube')
    created_at = models.DateTimeField(auto_now_add=True, null=True)


    def __str__(self):
        return self.title


    class Meta:
         verbose_name = 'книгу'
         verbose_name_plural = 'книги'
        
