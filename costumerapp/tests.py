from time import sleep
from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from core.utils import get_driver


class CostumerTestCase(TestCase):
    def test_signin(self):
        driver = get_driver()
        driver.get("http://127.0.0.1:8000/signin/")
        sleep(3)
        username_element = driver.find_element(By.NAME, "username")
        password_element = driver.find_element(By.ID, "id_password")

        username_element.clear()
        username_element.send_keys("admin")
        sleep(3)

        password_element.clear()
        password_element.send_keys("admin")
        sleep(3)
        password_element.send_keys(Keys.RETURN)
        assert "Вы успешно авторизовались!" in driver.page_source
        # sleep(5)
        # driver.get("http://localhost:8000/new-create/")
        # sleep(5)
        # button = driver.find_element(By.ID, "add-new")
        # button.click()
        sleep(5)

        driver.close()
