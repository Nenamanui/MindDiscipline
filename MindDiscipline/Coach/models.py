from django.db import models


class Coach(models.Model):
    nickname = models.CharField(max_length=50, blank=True, verbose_name='Никнейм (опционально)')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    first_name = models.CharField(max_length=15, verbose_name='Имя')
    patronymic_name = models.CharField(max_length=50, blank=True, verbose_name='Отчество (опционально)')
    main_sport = models.CharField(max_length=50, verbose_name='Основной вид спорта')
    extra_sport = models.CharField(max_length=50, blank=True, verbose_name='Дополнительный вид спорта')
    birthday = models.DateField(verbose_name='Дата рождения')
    experience_years = models.PositiveSmallIntegerField(verbose_name='Стаж')
    practice = models.ManyToManyField('practice.practice', verbose_name='Тренировки')

    class Meta:
        verbose_name = 'Тренер'
        verbose_name_plural = 'тренеры'

    def __str__(self):
        return self.last_name + ' ' + self.first_name + ' ' + self.patronymic_name