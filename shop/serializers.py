from rest_framework.serializers import ModelSerializer
 
from shop.models import Category, Product, Article
 
class CategorySerializer(ModelSerializer):
 
    class Meta:
        model = Category
        fields = ['id', 'name']

class ProductSerializer(ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'


class ArticleSerializer(ModelSerializer):

    class Meta:
        model = Article
        fields = '__all__'