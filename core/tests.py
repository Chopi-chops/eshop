from django.test import TestCase
from .factories import ProductFactory
from .models import Product
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from core.utils import get_driver
from time import sleep


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


class ProductProfileCreateTestCase(TestCase):
    def test_create_product_should_pass(self):
        driver = get_driver()
        driver.get("http://localhost:8000/product-create/")
        sleep(3)
        name_element = driver.find_element(By.NAME, "name")
        description_element = driver.find_element(By.NAME, "description")
        price_element = driver.find_element(By.NAME, "price")

        name_element.clear()
        name_element.send_keys("наушники")
        sleep(3)
        description_element.clear()
        description_element.send_keys("black")
        sleep(3)
        price_element.clear()
        price_element.send_keys("20000")
        sleep(3)
        button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'add-product'))
        )
        button.click()
        sleep(5)

        driver.close()

    def test_create_profile_should_pass(self):
        driver = get_driver()
        driver.get("http://localhost:8000/profile-create/")
        sleep(3)
        bio_element = driver.find_element(By.NAME, "bio")
        link_element = driver.find_element(By.NAME, "social_link")
        phone_element = driver.find_element(By.NAME, "phone_number")

        bio_element.clear()
        bio_element.send_keys("cool")
        sleep(3)
        link_element.clear()
        link_element.send_keys("black")
        sleep(3)
        phone_element.clear()
        phone_element.send_keys("12345")
        sleep(1)
        button = driver.find_element(By.ID, 'add-product')
        ActionChains(driver).scroll_to_element(button).perform()
        sleep(3)
        button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'add-profile'))
        )
        button.click()
        sleep(5)

        driver.close()

