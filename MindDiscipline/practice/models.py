from django.db import models


class Practice(models.Model):
    type = models.CharField(max_length=50)
    date = models.DateTimeField()
    duration = models.DurationField()
    main_theme = models.CharField(max_length=50)
    description = models.TextField()
    # coach = models.ForeignKey(Coach, on_delete=)
    child = models.ManyToManyField('child.Child')