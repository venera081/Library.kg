from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Clothe(models.Model):
    name_clothe = models.CharField(max_length=100)
    description = models.TextField(default='Одежда нужна для защиты от окружающей среды, например, от холода и жары.' \
    ' Кроме того, она выполняет информационную функцию, сигнализируя о социальном статусе, профессии и индивидуальности ' \
    'человека, а также эстетическую, помогая создавать образ и выражать себя. ')
    country = models.CharField(max_length=100)
    size = models.CharField(max_length=150, null=True)
    tags = models.ManyToManyField(Tag)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.name_clothe}-{", ".join(i.name for i in self.tags.all())}'
    

