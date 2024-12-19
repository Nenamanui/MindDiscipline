from django.db import models


class Child(models.Model):
    nickname = models.CharField(max_length=50, blank=True, verbose_name='Никнейм (опционально)')
    first_name = models.CharField(max_length=15, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    patronymic_name = models.CharField(max_length=50, blank=True, verbose_name='Отчество (опционально)')
    main_sport = models.CharField(max_length=50, verbose_name='Основной вид спорта')
    extra_sport = models.CharField(max_length=50, verbose_name='Дополнительный вид спорта')
    birthday = models.DateField(verbose_name='День Рождения')
    group = models.ForeignKey('group.group', on_delete=models.DO_NOTHING, verbose_name='Группа')
    practice = models.ManyToManyField('practice.practice')

    class Meta:
        verbose_name = 'Ребенок'
        verbose_name_plural = 'дети'

    def __str__(self):
        return self.first_name + ' ' + self.last_name

class Statistics(models.Model):
    pass 
    # attention = models.IntegerField(
    #    validators=[
    #        MinValueValidator(1),
    #       MaxValueValidator(10)
    #   ]
    #)
    # удачливость?
    # уверенность
    # настроение
    # ...
    # 