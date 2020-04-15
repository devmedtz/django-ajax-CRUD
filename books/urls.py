from django.urls import path, include
from . import views

app_name = 'books'

urlpatterns = [
    path('', views.book_list, name='book-list'),
]
