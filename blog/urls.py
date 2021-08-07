from django.urls import path
from . import views

urlpatterns = [
    path('articulos/', views.list, name="articulos"),
    path('categoria/<int:category_id>', views.category, name="categorias"),
    path('articulo/<int:article_id>', views.article, name="articulo"),
]