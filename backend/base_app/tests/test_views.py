from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from ..models import Product
from ..serializers import ProductSerializer

# initialize the APIClient app
client = APIClient()


class GetAllProductsTest(APITestCase):
    def setUp(self):
        Product.objects.create(name='Product1', category='Category1', brand='Brand1', description='Description1', rating=3.5, price=9.99, countInStock=10)
        Product.objects.create(name='Product2', category='Category2', brand='Brand2', description='Description2', rating=4.0, price=19.99, countInStock=20)
        Product.objects.create(name='Product3', category='Category3', brand='Brand3', description='Description3', rating=4.5, price=29.99, countInStock=30)
        Product.objects.create(name='Product4', category='Category4', brand='Brand4', description='Description4', rating=5.0, price=39.99, countInStock=40)

    def test_get_all_products(self):
        # get API response
        response = client.get(reverse('products'))
        # get data from db
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)