#!/usr/bin/env python
# -*- coding: utf-8 -*-
from settings import *

VERSION = "v1.43"
REGION = "US" # please note that "region" is required, despite anything that the docs says
API_KEY = '68LgCBmJcm6xM7fO1YQUB02UMKGvDk'
BASE_URL = "http://api-public.guidebox.com/%s/%s/%s" % (VERSION, REGION, API_KEY)
