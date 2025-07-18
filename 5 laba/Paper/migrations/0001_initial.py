# Generated by Django 5.2.1 on 2025-05-29 15:05

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name="Ім'я Автора")),
                ('bio', models.TextField(blank=True, null=True, verbose_name='Біографія')),
            ],
            options={
                'verbose_name': 'Автор',
                'verbose_name_plural': 'Автори',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Назва Книги')),
                ('publication_date', models.DateField(verbose_name='Дата публікації')),
                ('isbn', models.CharField(help_text='Міжнародний стандартний номер книги (13 цифр)', max_length=13, unique=True, verbose_name='ISBN')),
                ('genre', models.CharField(choices=[('FICTION', 'Художня література'), ('NON_FICTION', 'Науково-популярна література'), ('FANTASY', 'Фантастика'), ('SCIENCE', 'Наука'), ('HISTORY', 'Історія'), ('BIOGRAPHY', 'Біографія'), ('POETRY', 'Поезія'), ('OTHER', 'Інше')], default='FICTION', max_length=50, verbose_name='Жанр')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Ціна')),
                ('pages', models.IntegerField(blank=True, null=True, verbose_name='Кількість сторінок')),
                ('description', models.TextField(blank=True, verbose_name='Опис')),
                ('is_published', models.BooleanField(default=True, verbose_name='Опубліковано')),
                ('stock_count', models.IntegerField(default=0, verbose_name='Кількість на складі')),
                ('availability', models.CharField(choices=[('IN_STOCK', 'В наявності'), ('OUT_OF_STOCK', 'Немає в наявності'), ('PRE_ORDER', 'Передзамовлення')], default='IN_STOCK', max_length=20, verbose_name='Доступність')),
                ('cover_image_url', models.URLField(blank=True, max_length=500, null=True, verbose_name='Посилання на обкладинку')),
                ('last_updated', models.DateTimeField(auto_now=True, verbose_name='Останнє оновлення')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата створення запису')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='Paper.author', verbose_name='Автор')),
            ],
            options={
                'verbose_name': 'Книга',
                'verbose_name_plural': 'Книги',
                'ordering': ['title'],
            },
        ),
    ]
