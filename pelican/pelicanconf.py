#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import random

AUTHOR = u'Nasser'
SITENAME = u"Nasser's Blog"
SITETAGLINE = "42 is the answer!"
SITEURL = 'http://localhost:8000'

quotes = ["Hello",
          "Funny quotes goes here"]
SITEDESCR = quotes[random.randint(0, len(quotes)-1)]

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         #('Python.org', 'http://python.org/'),
         #('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
#SOCIAL = (('Google+', 'plus.google.com'),
          #('Twitter', 'nashamri.twitter.com'),)

GITHUB_URL = "https://github.com/nashamri/"
GOOGLE_URL = "https://plus.google.com/+nasseralshammari"
TWITTER_URL = "https://www.twitter.com/nashamri"
DEFAULT_PAGINATION = 4

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

#CSS_FILE = "wide.css"

TYPOGRIFY = True
THEME = "../lannisport"
SITELOGO = "img/site-logo.png"
#STATIC_PATHS = ["images", ]
