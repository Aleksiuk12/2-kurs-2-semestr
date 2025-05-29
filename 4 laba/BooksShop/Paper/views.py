from django.shortcuts import render

def index_view(request):
    context = {
        'title': 'Головна сторінка Книжкового Магазину',
        'links': [
            {'url_name': 'books', 'text': 'Наші Книги'},
            {'url_name': 'promotions', 'text': 'Акції та Знижки'},
            {'url_name': 'contact', 'text': 'Контакти'},
            {'url_name': 'novelties', 'text': 'Новинки'},
        ]
    }
    return render(request, 'Paper/index.html', context)

def books_view(request):
    context = {
        'title': 'Наші Книги',
        'content': 'Ознайомтеся з нашим широким асортиментом літератури різних жанрів.',
        'home_url_name': 'home' # Для посилання на головну
    }
    return render(request, 'Paper/generic_page.html', context)

def promotions_view(request):
    context = {
        'title': 'Акції та Знижки',
        'content': 'Дізнайтеся про наші гарячі пропозиції та спеціальні знижки на книги.',
        'home_url_name': 'home'
    }
    return render(request, 'Paper/generic_page.html', context)

def contact_view(request):
    context = {
        'title': 'Контакти',
        'content': 'Зв\'яжіться з нами за телефоном, електронною поштою або відвідайте наш офіс.',
        'home_url_name': 'home'
    }
    return render(request, 'Paper/generic_page.html', context)

def novelties_view(request):
    context = {
        'title': 'Новинки',
        'content': 'Відкрийте для себе останні надходження та найпопулярніші книги.',
        'home_url_name': 'home'
    }
    return render(request, 'Paper/generic_page.html', context)