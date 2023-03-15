from django.conf import settings
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase


class ShortenUrlViewTests(APITestCase):
    def setUp(self):
        self.shorten_url = reverse('shorten_url')
        self.data = dict(
            url='https://www.farsnews.ir/news/14011216000365/%D9%82%D8%B1%D8%B9%D9%87-%DA%A9%D8%B4%DB%8C-%D8%AC%D8%A7%D9%85-%D8%AD%D8%B0%D9%81%DB%8C-%D8%A7%D9%86%D8%AC%D8%A7%D9%85-%D8%B4%D8%AF%7C-%D8%A7%D8%B3%D8%AA%D9%82%D9%84%D8%A7%D9%84-%D8%AF%D8%B1-%D8%AC%D9%85-%D9%BE%D8%B1%D8%B3%D9%BE%D9%88%D9%84%DB%8C%D8%B3-%D8%AF%D8%B1-%D8%A7%D9%86%D8%AA%D8%B8%D8%A7%D8%B1-%D8%A8%D8%B1%D9%86%D8%AF%D9%87',
        )

    def test_shorten_url(self):
        response = self.client.post(
            self.shorten_url,
            data=self.data,
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn(settings.SITE_URL, response.data['short_id'])

    def test_shorten_url_data_invalidation(self):
        invalid_data = {'url': 'Not a valid url'}
        response = self.client.post(
            self.shorten_url,
            data=invalid_data,
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('Enter a valid URL.', response.data['url'])

    def test_get_original_url(self):
        response = self.client.post(
            self.shorten_url,
            data=self.data,
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn(settings.SITE_URL, response.data['short_id'])
        self.assertEqual(response.data['count'], 0)

        short_id = response.data['short_id'].replace(settings.SITE_URL, '')
        url_get = f'http://localhost:8000/{short_id}'
        response_get = self.client.get(url_get)
