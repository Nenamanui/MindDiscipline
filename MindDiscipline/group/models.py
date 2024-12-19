from django.db import models


class Group(models.Model):
    short_name = models.CharField(max_length=10, verbose_name='Короткое название')
    full_name = models.CharField(max_length=50, verbose_name='Полное название')
    sport = models.CharField(max_length=50, verbose_name='Вид спорта')
    coach = models.ForeignKey('coach.coach', on_delete=models.DO_NOTHING,verbose_name='Тренер')

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'группы'

    def __str__(self):
        return self.full_name