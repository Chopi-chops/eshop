from django.test import TestCase
from .factories import NewFactory
from .models import New

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
        form_data = {
            "title": "Тестовая новость 99",
            "article": "Что-то то там"
        }

        response = self.client.post(
            path="/new-create/",
            data=form_data
        )

        self.assertEqual(response.status_code, 302)
        query = New.objects.filter(
            title=form_data["title"],
            article=form_data["article"]
        )
        self.assertGreater(query.count(), 0)


