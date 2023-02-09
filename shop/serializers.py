from rest_framework.serializers import ModelSerializer 
from shop.models import Category, Product, Article

 
class ArticleSerializer(ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class CategorySerializer(ModelSerializer):
    
    products = ProductSerializer(many=True)
    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'active', 'created_at', 'updated_at', 'products']

    def get_products(self, instance):
        query_set = instance.products.filter(active=True)
        serializer = ProductSerializer(query_set, many=True)
        return serializer.data