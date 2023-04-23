from django.test import TestCase
from django.contrib.auth.models import User
from ..models import Product, Review, Order, OrderItem, ShippingAddress
from django.contrib.auth import get_user_model


class ProductModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        user = User.objects.create_user(
            username='testuser',
            password='12345'
        )
        Product.objects.create(
            user=user,
            name='Test Product',
            category='Test Category',
            brand='Test Brand',
            description='Test Description',
            rating=4.5,
            numReviews=10,
            price=99.99,
            countInStock=5
        )

    def test_name_label(self):
        product = Product.objects.get(_id=1)
        field_label = product._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_category_label(self):
        product = Product.objects.get(_id=1)
        field_label = product._meta.get_field('category').verbose_name
        self.assertEqual(field_label, 'category')

    def test_brand_label(self):
        product = Product.objects.get(_id=1)
        field_label = product._meta.get_field('brand').verbose_name
        self.assertEqual(field_label, 'brand')

    def test_description_label(self):
        product = Product.objects.get(_id=1)
        field_label = product._meta.get_field('description').verbose_name
        self.assertEqual(field_label, 'description')

    def test_rating_label(self):
        product = Product.objects.get(_id=1)
        field_label = product._meta.get_field('rating').verbose_name
        self.assertEqual(field_label, 'rating')

    def test_numReviews_label(self):
        product = Product.objects.get(_id=1)
        field_label = product._meta.get_field('numReviews').verbose_name
        self.assertEqual(field_label, 'numReviews')

    def test_price_label(self):
        product = Product.objects.get(_id=1)
        field_label = product._meta.get_field('price').verbose_name
        self.assertEqual(field_label, 'price')

    def test_countInStock_label(self):
        product = Product.objects.get(_id=1)
        field_label = product._meta.get_field('countInStock').verbose_name
        self.assertEqual(field_label, 'countInStock')

    def test_user_is_foreign_key(self):
        product = Product.objects.get(_id=1)
        self.assertEqual(product.user.username, 'testuser')

    def test_string_representation(self):
        product = Product.objects.get(_id=1)
        self.assertEqual(str(product), product.name)


class ReviewModelTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create(username='testuser')
        self.product = Product.objects.create(
            user=self.user,
            name='Test Product',
            rating=4.5,
            price=99.99,
            countInStock=10,
        )
        self.review = Review.objects.create(
            user=self.user,
            product=self.product,
            name='Test Review',
            rating=4,
            comment='This is a test review',
        )

    def test_review_creation(self):
        self.assertEqual(Review.objects.count(), 1)
        self.assertEqual(str(self.review), '4')
        self.assertEqual(self.review.user, self.user)
        self.assertEqual(self.review.product, self.product)
        self.assertEqual(self.review.name, 'Test Review')
        self.assertEqual(self.review.rating, 4)
        self.assertEqual(self.review.comment, 'This is a test review')


class OrderItemModelTestCase(TestCase):
    def setUp(self):
        # Create a user
        self.user = User.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='testpass'
        )

        # Create a product
        self.product = Product.objects.create(
            user=self.user,
            name='Test Product',
            category='Test Category',
            brand='Test Brand',
            description='Test Description',
            rating=4.5,
            numReviews=10,
            price=19.99,
            countInStock=5
        )

        # Create an order
        self.order = Order.objects.create(
            user=self.user,
            paymentMethod='paypal',
            taxPrice=2.00,
            shippingPrice=5.00,
            totalPrice=26.99,
            isPaid=True,
            paidAt='2022-04-23 12:00:00',
            isDelivered=False
        )

        # Create an order item
        self.order_item = OrderItem.objects.create(
            product=self.product,
            order=self.order,
            name=self.product.name,
            qty=2,
            price=self.product.price,
            image='test_image.jpg'
        )

    def test_order_item_fields(self):
        """
        Test that the OrderItem model fields were created correctly.
        """
        self.assertEqual(self.order_item.product, self.product)
        self.assertEqual(self.order_item.order, self.order)
        self.assertEqual(self.order_item.name, 'Test Product')
        self.assertEqual(self.order_item.qty, 2)
        self.assertEqual(self.order_item.price, 19.99)
        self.assertEqual(self.order_item.image, 'test_image.jpg')

    def test_order_item_string_representation(self):
        """
        Test that the string representation of an OrderItem object is correct.
        """
        self.assertEqual(str(self.order_item), 'Test Product')


