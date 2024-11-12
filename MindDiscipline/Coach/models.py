from django.db import models


class Coach(models.Model):
    nickname = models.CharField(max_length=50)
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=50)
    main_sport = models.CharField(max_length=50)
    extra_sport = models.CharField(max_length=50)
    birthday = models.DateField()
    experience_date = models.PositiveSmallIntegerField()
    practice = models.ManyToManyField('practice.practice')