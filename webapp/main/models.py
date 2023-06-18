from django.db import models

class Articles(models.Model):
    name = models.CharField('ФИО', max_length=250)
    number = models.CharField('Номер телефона', max_length=250)
    email = models.EmailField('Email')
    app = models.CharField('Введите сообщение',max_length=250)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'