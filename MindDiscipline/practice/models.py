from django.db import models


class Practice(models.Model):
    type = models.CharField(max_length=50, verbose_name='Наименование тренировки')
    date = models.DateTimeField('Дата')
    duration = models.DurationField('Длительность')
    main_theme = models.CharField(max_length=50, verbose_name='Основная тема тренировки')
    description = models.CharField(max_length=600, verbose_name='Описание')
    group = models.ForeignKey('group.group', on_delete=models.DO_NOTHING, verbose_name='Группа')

    class Meta:
        verbose_name = 'Тренировка'
        verbose_name_plural = 'тренировки'

    def __str__(self):
        return self.type + ' ' + self.main_theme