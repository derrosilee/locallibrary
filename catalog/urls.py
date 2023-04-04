from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', BookListView.as_view(), name='books')
]
