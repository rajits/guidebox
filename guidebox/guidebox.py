from django.conf import settings
from utils import get_dict

SOURCES = ("free", "tv_everywhere", "subscription", "purchase", "all")
PLATFORMS = ("web", "ios", "android", "all")

def list_regions():
    d = get_dict(settings.BASE_URL + "/regions/all")

    return [result['region'] for result in d['results']]

def get_all_shows(limit1=50, limit=25):
    url = settings.BASE_URL + "/shows/all/%s/%s/all/all" % (limit1, limit2)
    d = get_dict(url)

    return [result['title'] for result in d['results']]

def get_show_information(id):
    url = settings.BASE_URL + "/show/" + id
    d = get_dict(url)

    return d['results'][0]['title']
