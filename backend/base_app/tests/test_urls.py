from django.test import SimpleTestCase
from django.urls import reverse, resolve
from ..views import routers, getProducts, getProduct


class TestUrls(SimpleTestCase):
    def test_routers_url_resolves(self):
        url = reverse('routers')
        self.assertEqual(resolve(url).func, routers)

    def test_products_url_resolves(self):
        url = reverse('products')
        self.assertEqual(resolve(url).func, getProducts)

    def test_product_url_resolves(self):
        url = reverse('product', args=['1'])
        self.assertEqual(resolve(url).func, getProduct)
