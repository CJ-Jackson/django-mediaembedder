from django.test import TestCase

class MediaEmbedderTestCase(TestCase):
    def setUp(self):
        from .models import Cache
        self.cache = Cache.objects.create(hash='Test', data='Test')

    def test_for_error_in_setup(self):
        self.assertEqual(self.cache.hash, 'Test')
        self.assertEqual(self.cache.data, 'Test')

    def tearDown(self):
        self.cache.delete()

