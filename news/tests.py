from django.test import TestCase
from .factories import NewFactory
from .models import New
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from core.utils import get_driver
from time import sleep

# Create your tests here.


class NewsListTestCase(TestCase):
    def setUp(self):
        self.new_object_1 = NewFactory()
        new_object_2 = NewFactory(title="Погода на сегодня")

    def test_open_list_should_success(self):
        url = '/news/'
        response = self.client.get(path=url)
        # assert response.status_code == 200
        self.assertEqual(response.status_code, 200, "список новостей: статус не 200")

    def test_open_list_should_show_list(self):
        url = '/news/'
        response = self.client.get(path=url)
        self.assertContains(response, self.new_object_1.title)
        self.assertContains(response, "Погода на сегодня")
        # print(New.objects.count())

    def test_open_one_new_should_success(self):
        url = '/new/1/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.new_object_1.title)
        self.assertContains(response, self.new_object_1.article)


class NewCreateTestCase(TestCase):
    def test_create_new_should_pass(self):
        driver = get_driver()
        driver.get("http://localhost:8000/new-create/")
        sleep(3)
        title_element = driver.find_element(By.NAME, "title")
        article_element = driver.find_element(By.NAME, "article")

        title_element.clear()
        title_element.send_keys("weather")
        sleep(3)
        article_element.clear()
        article_element.send_keys("good")
        sleep(3)
        button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'add-new'))
        )
        button.click()
        sleep(5)

        driver.close()


