#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Andrew Ma'
SITENAME = u'Andrew Ma'
SITEURL = ''

ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
CATEGORY_URL = 'category/{slug}/'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'
TAG_URL = 'tag/{slug}/'
TAG_SAVE_AS = 'tag/{slug}/index.html'
AUTHOR_URL = 'author/{slug}/'
AUTHOR_SAVE_AS = 'author/{slug}/index.html'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('Pelican', 'http://getpelican.com/'),
          ('Python.org', 'http://python.org/'),
          ('Jinja2', 'http://jinja.pocoo.org/'),)

# Social widget
SOCIAL = (('Github', 'https://github.com/ajma'),
          ('LinkedIn', 'http://www.linkedin.com/in/andrewma'),
          ('Google+', 'https://plus.google.com/111239791981124653981?rel=author'),
          ('Stackoverflow', 'http://stackoverflow.com/users/60117'),)

DEFAULT_PAGINATION = 10

DISQUS_SITENAME = 'ajma'
GOOGLE_ANALYTICS = 'UA-19274340-1'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
