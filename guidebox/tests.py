from django.test import TestCase
from models import Show

class ShowTestCase(TestCase):
    def test_title(self):
        show = Show.create(13015)
        self.assertEqual(show.get_title(), "Arrow")
