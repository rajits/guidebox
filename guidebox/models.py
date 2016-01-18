from django.conf import settings
from django.db import models

from utils import get_dict

class Show(models.Model):
    show_id = models.IntegerField()

    @classmethod
    def create(cls, show_id):
        show = cls(show_id=show_id)
        url = settings.BASE_URL + "/show/" + id
        show.d = get_dict(url)['results'][0]

        return show

    def get_attr(attr):
        return self.d[attr]

    def get_title():
        return get_attr('title')
