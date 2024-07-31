from django.test import TestCase
from .factories import ProductFactory
from .models import Product


class ProductsListTestCase(TestCase):
    def setUp(self):
        self.product_object_1 = ProductFactory()
        product_object_2 = ProductFactory(name="Телефон xiaomi")

    def test_open_list_should_show_list(self):
        url = '/'
        response = self.client.get(path=url)
        self.assertContains(response, self.product_object_1.name)
        self.assertContains(response, self.product_object_1.price)
        self.assertContains(response, self.product_object_1.qty)
        self.assertContains(response, "xiaomi")

    def test_open_one_product_should_success(self):
        url = '/product/1/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.product_object_1.name)
        self.assertContains(response, self.product_object_1.description)


class ProductCreateTestCase(TestCase):
    def test_create_product_should_pass(self):
        form_data = {
            "name": "Тестовый товар 1",
            "description": "Что-то то там",
            "price": "111",
            "qty": "111"
        }

        response = self.client.post(
            path="/product-create/",
            data=form_data
        )

        self.assertEqual(response.status_code, 200)
        query = Product.objects.filter(
            name=form_data["name"],
            description=form_data["description"],
            price=form_data["price"],
            qty=form_data["qty"]
        )
        self.assertGreater(query.count(), 0)

