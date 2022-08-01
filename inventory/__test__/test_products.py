from rest_framework.test import APITestCase
from inventory.models import Product
from django.urls import reverse
from rest_framework import status
from django.test import TestCase


class ProductTest(TestCase):

    def setUp(self):

        self.product = Product.objects.create(name='Product 1', price=10.00)

    def test_product_iva(self):
        self.assertEqual(self.product.get_product_with_iva(), 11.90)