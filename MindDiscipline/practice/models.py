from django.db import models


class Practice(models.Model):
    type = models.CharField(max_length=50)
    date = models.DateTimeField('Дата')
    duration = models.DurationField()
    main_theme = models.CharField(max_length=50)
    description = models.TextField()
    child = models.ManyToManyField('child.Child')