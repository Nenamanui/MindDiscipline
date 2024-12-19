# Generated by Django 5.1.2 on 2024-12-19 20:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('child', '0001_initial'),
        ('group', '0002_alter_group_options'),
        ('practice', '0004_alter_practice_options_remove_practice_child_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='child',
            options={'verbose_name': 'Ребенок', 'verbose_name_plural': 'дети'},
        ),
        migrations.AddField(
            model_name='child',
            name='group',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='group.group', verbose_name='Группа'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='child',
            name='patronymic_name',
            field=models.CharField(blank=True, max_length=50, verbose_name='Отчество (опционально)'),
        ),
        migrations.AddField(
            model_name='child',
            name='practice',
            field=models.ManyToManyField(to='practice.practice'),
        ),
        migrations.AlterField(
            model_name='child',
            name='birthday',
            field=models.DateField(verbose_name='День Рождения'),
        ),
        migrations.AlterField(
            model_name='child',
            name='extra_sport',
            field=models.CharField(max_length=50, verbose_name='Дополнительный вид спорта'),
        ),
        migrations.AlterField(
            model_name='child',
            name='first_name',
            field=models.CharField(max_length=15, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='child',
            name='last_name',
            field=models.CharField(max_length=50, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='child',
            name='main_sport',
            field=models.CharField(max_length=50, verbose_name='Основной вид спорта'),
        ),
        migrations.AlterField(
            model_name='child',
            name='nickname',
            field=models.CharField(blank=True, max_length=50, verbose_name='Никнейм (опционально)'),
        ),
    ]
