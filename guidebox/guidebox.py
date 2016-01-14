import ast, requests
from django.conf import settings

SOURCES = ("free", "tv_everywhere", "subscription", "purchase", "all")
PLATFORMS = ("web", "ios", "android", "all")

def list_regions():
    url = settings.BASE_URL + "/regions/all"
    f = requests.get(url)
    d = ast.literal_eval(f.text)

    return [result['region'] for result in d['results']]

def get_all_shows(limit1, limit2):
    if not limit1:
        limit1 = 50
    if not limit2:
        limit2 = 25
    url = settings.BASE_URL + "/shows/all/%s/%s/all/all" % (limit1, limit2)
    f = requests.get(url)
    d = ast.literal_eval(f.text)

    return [result['title'] for result in d['results']]

def get_show_information(id):
    url = settings.BASE_URL + "/show/" + id
    f = requests.get(url)
    d = ast.literal_eval(f.text)

    return [result['title'] for result in d['results']]
