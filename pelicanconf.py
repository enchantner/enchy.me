#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'enchantner'
SITENAME = "Engineer's Lair"
SITEURL = ''

PATH = 'content'

THEME = 'themes/pelican-elegant-1.3'
JINJA_EXTENSIONS = ['jinja2.ext.i18n']

TIMEZONE = 'Europe/Moscow'

DEFAULT_LANG = 'en'
LOCALE = 'en_US.UTF-8'

I18N_SUBSITES = {
    'ru': {
        'SITENAME': 'Берлога инженера',
        'LOCALE': 'ru_RU.UTF-8',
        'THEME': 'themes/pelican-elegant-1.3'
    }
}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

MARKUP = ('md', 'ipynb')
PLUGIN_PATHS = ['./plugins']
PLUGINS = ['ipynb', 'i18n_subsites']

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
