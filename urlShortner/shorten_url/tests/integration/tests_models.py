from django.test import TestCase

from shorten_url.models import ShortUrlModel


class ShortUrlModelIntegrationTests(TestCase):
    def setUp(self):
        self.data = dict(
            url='https://www.farsnews.ir/news/14011216000365/%D9%82%D8%B1%D8%B9%D9%87-%DA%A9%D8%B4%DB%8C-%D8%AC%D8%A7%D9%85-%D8%AD%D8%B0%D9%81%DB%8C-%D8%A7%D9%86%D8%AC%D8%A7%D9%85-%D8%B4%D8%AF%7C-%D8%A7%D8%B3%D8%AA%D9%82%D9%84%D8%A7%D9%84-%D8%AF%D8%B1-%D8%AC%D9%85-%D9%BE%D8%B1%D8%B3%D9%BE%D9%88%D9%84%DB%8C%D8%B3-%D8%AF%D8%B1-%D8%A7%D9%86%D8%AA%D8%B8%D8%A7%D8%B1-%D8%A8%D8%B1%D9%86%D8%AF%D9%87',
            short_id='7svkz3',
        )
        self.url_obj = ShortUrlModel.objects.create(**self.data)

    def test_increase_url_counter(self):
        url_obj = ShortUrlModel.objects.get(short_id=self.data['short_id'])

        self.assertEqual(url_obj.count, 0)
        url_obj.increase_short_id_counter()
        self.assertEqual(url_obj.count, 1)

    def test_generate_short_id(self):
        short_id = ShortUrlModel.generate_short_id()

        self.assertEqual(len(short_id), ShortUrlModel.ID_LENGTH)
