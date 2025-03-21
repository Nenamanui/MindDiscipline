# Generated by Django 5.1.2 on 2024-12-11 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coach', '0004_rename_experience_date_coach_experience_years'),
        ('practice', '0002_practice_child'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='coach',
            options={'verbose_name': 'Тренер', 'verbose_name_plural': 'тренеры'},
        ),
        migrations.AddField(
            model_name='coach',
            name='patronymic_name',
            field=models.CharField(blank=True, max_length=50, verbose_name='Отчество (опционально)'),
        ),
        migrations.AlterField(
            model_name='coach',
            name='birthday',
            field=models.DateField(verbose_name='Дата рождения'),
        ),
        migrations.AlterField(
            model_name='coach',
            name='experience_years',
            field=models.PositiveSmallIntegerField(verbose_name='Стаж'),
        ),
        migrations.AlterField(
            model_name='coach',
            name='extra_sport',
            field=models.CharField(max_length=50, verbose_name='Дополнительный вид спорта'),
        ),
        migrations.AlterField(
            model_name='coach',
            name='first_name',
            field=models.CharField(max_length=15, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='coach',
            name='last_name',
            field=models.CharField(max_length=50, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='coach',
            name='main_sport',
            field=models.CharField(max_length=50, verbose_name='Основной вид спорта'),
        ),
        migrations.AlterField(
            model_name='coach',
            name='nickname',
            field=models.CharField(blank=True, max_length=50, verbose_name='Никнейм (опционально)'),
        ),
        migrations.AlterField(
            model_name='coach',
            name='practice',
            field=models.ManyToManyField(to='practice.practice', verbose_name='Тренировки'),
        ),
    ]
