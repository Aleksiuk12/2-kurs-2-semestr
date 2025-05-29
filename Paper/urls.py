from django.urls import path
from . import views

app_name = 'Paper'

urlpatterns = [
    path('', views.index_view, name='home'),
    path('books/', views.books_view, name='books'),
    path('promotions/', views.promotions_view, name='promotions'),
    path('contact/', views.contact_view, name='contact'),
    path('novelties/', views.novelties_view, name='novelties'),
]