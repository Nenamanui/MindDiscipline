from django.db import models


class Child(models.Model):
    nickname = models.CharField(max_length=50)
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=50)
    main_sport = models.CharField(max_length=50)
    extra_sport = models.CharField(max_length=50)
    birthday = models.DateField()

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