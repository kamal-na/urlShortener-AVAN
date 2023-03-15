from django.test import TestCase

from shorten_url.models import ShortUrlModel
from shorten_url.serializers import ShortUrlSerializer


class ShortUrlSerializerUnitTests(TestCase):
    def setUp(self):
        self.blank_data = dict(
            url='',
            short_id='',
        )
        self.wrong_data = dict(
            url='I am not a url',
            short_id='I am not a valid code',
        )

    def test_url_serializer_required_fields(self):
        serializer = ShortUrlSerializer(data=self.blank_data)
        serializer.is_valid()

        self.assertIn('This field may not be blank.', serializer.errors['url'])
        self.assertIn('This field may not be blank.', serializer.errors['short_id'])

    def test_url_serializer_wrong_data(self):
        serializer = ShortUrlSerializer(data=self.wrong_data)
        serializer.is_valid()

        self.assertIn('Enter a valid URL.', serializer.errors['url'])
        self.assertIn(f'Ensure this field has no more than {ShortUrlModel.ID_LENGTH} characters.',
                      serializer.errors['short_id'])
