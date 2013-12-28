#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import random

AUTHOR = u'Nasser'
SITENAME = u"Nasser's Blog"
SITETAGLINE = "42 is the answer!"
SITEURL = 'http://www.nass3r.com'

quotes = ["I do not agree with what you have to say, but I'll defend to the death your right to say it. --Voltaire",
          "Common sense is not so common. --Voltaire",
          "Judge a man by his questions rather than his answers. --Voltaire",
          "It is dangerous to be right in matters on which the established authorities are wrong. --Voltaire",
          "Doubt is not a pleasant condition, but certainty is absurd. --Voltaire",
          "A witty saying proves nothing. --Voltaire",
          "If you tell the truth, you don't have to remember anything. --Mark Twain",
          "Go to Heaven for the climate, Hell for the company. --Mark Twain",
          "It is better to remain silent and be thought a fool than to open one's mouth and remove all doubt. --Mark Twain",
          "Whenever you find yourself on the side of the majority, it is time to pause and reflect. --Mark Twain"]
SITEDESCR = quotes[random.randint(0, len(quotes)-1)]

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

GOOGLE_ANALYTICS_CODE = 'UA-36815966-1'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
#SOCIAL = (('Google+', 'plus.google.com'),
          #('Twitter', 'nashamri.twitter.com'),)

GITHUB_URL = "https://github.com/nashamri/"
GOOGLE_URL = "https://plus.google.com/+nasseralshammari"
TWITTER_URL = "https://www.twitter.com/nashamri"
LINKEDIN_URL = "http://www.linkedin.com/pub/nasser-alshammari/88/799/834"

DEFAULT_PAGINATION = 4

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

#CSS_FILE = "wide.css"

TYPOGRIFY = True
THEME = "../lannisport"
SITELOGO = "img/site-logo.png"
#STATIC_PATHS = ["images", ]
