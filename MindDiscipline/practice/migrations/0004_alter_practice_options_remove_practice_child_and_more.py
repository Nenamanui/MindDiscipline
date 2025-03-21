# Generated by Django 5.1.2 on 2024-12-19 20:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0002_alter_group_options'),
        ('practice', '0003_alter_practice_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='practice',
            options={'verbose_name': 'Тренировка', 'verbose_name_plural': 'тренировки'},
        ),
        migrations.RemoveField(
            model_name='practice',
            name='child',
        ),
        migrations.AddField(
            model_name='practice',
            name='group',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='group.group', verbose_name='Группа'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='practice',
            name='description',
            field=models.CharField(max_length=600, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='practice',
            name='duration',
            field=models.DurationField(verbose_name='Длительность'),
        ),
        migrations.AlterField(
            model_name='practice',
            name='main_theme',
            field=models.CharField(max_length=50, verbose_name='Основная тема тренировки'),
        ),
        migrations.AlterField(
            model_name='practice',
            name='type',
            field=models.CharField(max_length=50, verbose_name='Наименование тренировки'),
        ),
    ]
