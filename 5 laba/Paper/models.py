from django.db import models
from django.utils import timezone

class Author(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Ім'я Автора")
    bio = models.TextField(blank=True, null=True, verbose_name="Біографія")

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Автори"
        ordering = ['name']

    def __str__(self):
        return self.name

GENRE_CHOICES = [
    ('FICTION', 'Художня література'),
    ('NON_FICTION', 'Науково-популярна література'),
    ('FANTASY', 'Фантастика'),
    ('SCIENCE', 'Наука'),
    ('HISTORY', 'Історія'),
    ('BIOGRAPHY', 'Біографія'),
    ('POETRY', 'Поезія'),
    ('OTHER', 'Інше'),
]

AVAILABILITY_STATUS = [
    ('IN_STOCK', 'В наявності'),
    ('OUT_OF_STOCK', 'Немає в наявності'),
    ('PRE_ORDER', 'Передзамовлення'),
]

class Book(models.Model):
    title = models.CharField(max_length=200, verbose_name="Назва Книги") # max_length: максимальна довжина
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books', verbose_name="Автор") # ForeignKey: зв'язок "багато до одного"
    publication_date = models.DateField(verbose_name="Дата публікації")
    isbn = models.CharField(max_length=13, unique=True, verbose_name="ISBN", help_text="Міжнародний стандартний номер книги (13 цифр)") # unique, help_text
    genre = models.CharField(max_length=50, choices=GENRE_CHOICES, default='FICTION', verbose_name="Жанр") # choices, default
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Ціна") # max_digits, decimal_places
    pages = models.IntegerField(blank=True, null=True, verbose_name="Кількість сторінок") # blank, null
    description = models.TextField(blank=True, verbose_name="Опис") # blank
    is_published = models.BooleanField(default=True, verbose_name="Опубліковано") # default
    stock_count = models.IntegerField(default=0, verbose_name="Кількість на складі") # default
    availability = models.CharField(max_length=20, choices=AVAILABILITY_STATUS, default='IN_STOCK', verbose_name="Доступність") # choices, default

    cover_image_url = models.URLField(max_length=500, blank=True, null=True, verbose_name="Посилання на обкладинку") # null, blank
    last_updated = models.DateTimeField(auto_now=True, verbose_name="Останнє оновлення") # auto_now: оновлюється при кожному збереженні
    created_at = models.DateTimeField(default=timezone.now, verbose_name="Дата створення запису") # default з timezone.now()

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"
        ordering = ['title']

    def __str__(self):
        return f"{self.title} by {self.author.name}"