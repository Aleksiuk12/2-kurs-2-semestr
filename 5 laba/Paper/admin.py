from django.contrib import admin
from .models import Author, Book

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'bio')
    search_fields = ('name',)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'genre', 'price', 'is_published', 'stock_count', 'availability') 
    list_filter = ('genre', 'is_published', 'availability', 'publication_date')
    search_fields = ('title', 'isbn', 'author__name')
    raw_id_fields = ('author',)
    fieldsets = (
        (None, {
            'fields': ('title', 'author', 'isbn', 'cover_image_url')
        }),
        ('Деталі Книги', {
            'fields': ('genre', 'publication_date', 'pages', 'price', 'description'),
            'classes': ('collapse',),
        }),
        ('Управління Запасами', {
            'fields': ('stock_count', 'availability', 'is_published'),
        }),
        ('Дати', {
            'fields': ('created_at', 'last_updated'),
            'classes': ('collapse',),
            'description': 'Автоматично оновлювані поля.'
        }),
    )
    readonly_fields = ('created_at', 'last_updated')
