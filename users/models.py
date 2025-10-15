from django.db import models


class WorkerProfile(models.Model):
    username = models.CharField(max_length=100, verbose_name="ФИО", null=True, unique=True)
    phone_number = models.CharField(max_length=14, default="+996")
    work = models.CharField(max_length=100, verbose_name='На какую должность вы претендуете?')
    skill = models.TextField(verbose_name='Какие навыки у вас имеются?')
    experience_work = models.CharField(max_length=100, verbose_name="Сколько лет/месяцев у вас есть опыт?")
    url_github = models.URLField(verbose_name="Скиньте свою ссылку на GitHub")
    image = models.ImageField(upload_to="certificates/", verbose_name="Вставьте ваш диплом/сертификат")
    email = models.EmailField(verbose_name="Введите вашу электронную почту", null=True, blank=True)
    birthday = models.CharField(max_length=100, verbose_name="День Рождения", null=True)
    address = models.CharField(max_length=100, verbose_name="Ваш адрес проживания", null=True)
    password = models.CharField(max_length=100, verbose_name="Пароль", null=True)  
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
