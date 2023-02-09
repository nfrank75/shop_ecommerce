from django.urls import path
from .views import CategoryViewset, ProductViewset,  ArticleViewset

urlpatterns = [
    path('category/', CategoryViewset),
    path('product/', ProductViewset),
    path('article/', ArticleViewset),
]
