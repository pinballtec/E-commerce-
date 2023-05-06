from django.test import TestCase
from django.contrib.auth.models import User
from ..models import Product
from ..serializers import ProductSerializer


class ProductSerializerTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='testpass')
        self.product = Product.objects.create(
            user=self.user,
            name='Test Product',
            category='Test Category',
            brand='Test Brand',
            description='Test description',
            rating=4.5,
            numReviews=10,
            price=99.99,
            countInStock=5
        )
        self.serializer = ProductSerializer(instance=self.product)

    def test_product_serializer(self):
        data = self.serializer.data
        self.assertEqual(data['id'], self.product.id)
        self.assertEqual(data['user'], str(self.user.id))
        self.assertEqual(data['name'], 'Test Product')
        self.assertEqual(data['category'], 'Test Category')
        self.assertEqual(data['brand'], 'Test Brand')
        self.assertEqual(data['description'], 'Test description')
        self.assertEqual(float(data['rating']), 4.5)
        self.assertEqual(data['numReviews'], 10)
        self.assertEqual(float(data['price']), 99.99)
        self.assertEqual(data['countInStock'], 5)

    def test_product_serializer_create(self):
        data = {
            'user': self.user.id,
            'name': 'New Product',
            'category': 'New Category',
            'brand': 'New Brand',
            'description': 'New description',
            'rating': 4.0,
            'numReviews': 5,
            'price': 49.99,
            'countInStock': 2
        }
        serializer = ProductSerializer(data=data)
        serializer.is_valid()
        product = serializer.save()
        self.assertEqual(product.user, self.user)
        self.assertEqual(product.name, 'New Product')
        self.assertEqual(product.category, 'New Category')
        self.assertEqual(product.brand, 'New Brand')
        self.assertEqual(product.description, 'New description')
        self.assertEqual(float(product.rating), 4.0)
        self.assertEqual(product.numReviews, 5)
        self.assertEqual(float(product.price), 49.99)
        self.assertEqual(product.countInStock, 2)
