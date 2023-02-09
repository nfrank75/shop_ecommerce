from django.urls import reverse_lazy, reverse
from rest_framework.test import APITestCase

from shop.models import Category, Product


class ShopApiTestCase():
    def format_datetime(self, value):
        # Cette méthode est un helper permettant de formater une date en chaine de caractères sous le même format que celui de l’api
        return value.strftime("%Y-%m-%dT%H:%M:%S.%fZ")


# class TestCategory(APITestCase, ShopApiTestCase):
#     # Nous stockons l’url de l'endpoint dans un attribut de classe pour pouvoir l’utiliser plus facilement dans chacun de nos tests
#     url = reverse_lazy('category-list')

#     def test_list(self):
#         # Créons deux catégories dont une seule est active
#         category = Category.objects.create(name='Pasteque', active=True)
#         Category.objects.create(name='Mangue', active=False)

#         # On réalise l’appel en GET en utilisant le client de la classe de test
#         response = self.client.get(self.url)
#         # Nous vérifions que le status code est bien 200
#         # et que les valeurs retournées sont bien celles attendues
#         self.assertEqual(response.status_code, 200)
#         excepted = [
#             {
#                 'id': category.id,
#                 'name': category.name,
#                 'created_at': self.format_datetime(category.created_at),
#                 'updated_at': self.format_datetime(category.updated_at),
#             }
#         ]
#         self.assertEqual(response.json(), excepted)

#     def test_create(self):
#         # Nous vérifions qu’aucune catégorie n'existe avant de tenter d’en créer une
#         self.assertFalse(Category.objects.exists())
#         response = self.client.post(self.url, data={'name': 'New Category'})
#         # Vérifions que le status code est bien en erreur et nous empêche de créer une catégorie
#         self.assertEqual(response.status_code, 405)
#         # Enfin, vérifions qu'aucune nouvelle catégorie n’a été créée malgré le status code 405
#         self.assertFalse(Category.objects.exists())


class TestProduct(APITestCase, ShopApiTestCase):
    url = reverse_lazy('product-list')

    def test_list(self):
        response = self.client.get(self.url)
        print(response.json())
        # Nous vérifions que le status code est bien 200
        self.assertEqual(response.status_code, 200)
        # verifions que les donnees retournes sont celles que nous attendons
        product = Product.objects.create(name='Telephone Tecno', description='Android Phone')
        Product.objects.create(name='Samsung Phone', description='Samsung Phone')
        expected_data = [{
                'id': product.id,
                'name': product.name,
                'created_at': self.format_datetime(product.created_at),
                'updated_at': self.format_datetime(product.updated_at),
            }]
        self.assertEqual(response.json(), expected_data) 
        
            

    


