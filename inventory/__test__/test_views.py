import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from inventory.models import Product
from inventory.serializers import ProductModelSerializer

client = Client()


class GetAllProductTest(TestCase):

    def setUp(self):
        Product.objects.create(name='Product 1', price=10.00)
        Product.objects.create(name='Product 2', price=20.00)
        Product.objects.create(name='Product 3', price=30.00)

    def test_get_all_product(self):
        # response = client.get(reverse('products-list'))
        response = client.get('/api/products/')
        products = Product.objects.all()
        serializer = ProductModelSerializer(products, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetSingleProductTest(TestCase):

    def setUp(self):
        self.product1 = Product.objects.create(name='Product 1', price=10.00)
        self.product2 = Product.objects.create(name='Product 2', price=20.00)
        self.product3 = Product.objects.create(name='Product 3', price=30.00)

    def test_get_valid_single_product(self):

        response = client.get('/api/products/{}/'.format(self.product1.id))
        serializer = ProductModelSerializer(self.product1)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_product(self):
        response = client.get('/api/products/{}/'.format(100))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class CreateNewProductTest(TestCase):

    def setUp(self):
        self.valid_payload = {
            'name': 'Product 1',
            'price': 10.00
        }
        self.invalid_payload = {
            'name': '',
            'price': ''
        }

    def test_create_valid_product(self):
        response = client.post(
            '/api/products/', data=json.dumps(self.valid_payload), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_product(self):
        response = client.post(
            '/api/products/', data=json.dumps(self.invalid_payload), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class UpdateSingleProduct(TestCase):

    def setUp(self):

        self.product1 = Product.objects.create(name='Product 1', price=10.00)
        self.product2 = Product.objects.create(name='Product 2', price=20.00)
        self.product3 = Product.objects.create(name='Product 3', price=30.00)

        self.valid_payload = {
            'name': 'Product 12',
            'price': 15.00
        }
        self.invalid_payload = {
            'name': '',
            'price': ''
        }

    def test_update_valid_product(self):
        response = client.put(
            '/api/products/{}/'.format(self.product1.id), data=json.dumps(self.valid_payload), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_invalid_update_product(self):
        response = client.put(
            '/api/products/{}/'.format(self.product1.id), data=json.dumps(self.invalid_payload), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class DeleteSingleProduct(TestCase):

    def setUp(self):

        self.product1 = Product.objects.create(name='Product 1', price=10.00)
        self.product2 = Product.objects.create(name='Product 2', price=20.00)
        self.product3 = Product.objects.create(name='Product 3', price=30.00)

    def test_delete_valid_product(self):
        response = client.delete(
            '/api/products/{}/'.format(self.product1.id))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_product(self):
        response = client.delete(
            '/api/products/{}/'.format(100))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)