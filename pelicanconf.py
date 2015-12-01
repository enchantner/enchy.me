#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Nikolay Markov'
SITENAME = 'Engineer\'s lair'
SITEURL = ''

PATH = 'content'

JINJA_EXTENSIONS = ['jinja2.ext.i18n']
THEME = 'themes/phased'

TIMEZONE = 'Europe/Moscow'

DEFAULT_LANG = 'en'
LOCALE = 'en_US.UTF-8'

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

# DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
MENUITEMS = (
    ('Blog', '/blog/index.html'),
    ('About me', SITEURL + '#about-me'),
)

# put articles (posts) in blog/
ARTICLE_URL = 'blog/{slug}.html'
ARTICLE_SAVE_AS = 'blog/{slug}.html'
# we need to change the main index page now though...
INDEX_SAVE_AS = 'blog/index.html'
INDEX_URL = 'blog/'
#now move all the category and tag stuff to that blog/ dir as well
CATEGORY_URL = 'blog/category/{slug}.html'
CATEGORY_SAVE_AS = 'blog/category/{slug}.html'
CATEGORIES_URL = 'blog/category/'
CATEGORIES_SAVE_AS = 'blog/category/index.html'
TAG_URL = 'blog/tag/{slug}.html'
TAG_SAVE_AS = 'blog/tag/{slug}.html'
TAGS_URL = 'blog/tag/'
TAGS_SAVE_AS = 'blog/tag/index.html'
ARCHIVES_SAVE_AS = 'blog/archives/archives.html'
ARCHIVES_URL = 'blog/archives/archives.html'
AUTHOR_SAVE_AS = 'blog/{slug}.html'
AUTHORS_SAVE_AS = 'blog/authors.html'
# put pages in the root directory
PAGE_SAVE_AS = '{slug}.html'
PAGE_URL = '{slug}.html'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

MARKUP = ('md', 'ipynb')
PLUGIN_PATHS = ['./plugins']
PLUGINS = [
    'ipynb',
    'tipue_search',
    'sitemap',
    'disqus_static'
]

STATIC_PATHS = ['images']

IPYNB_USE_META_SUMMARY = True

TYPOGRIFY = True

DISQUS_SITENAME = 'enchyme'
DISQUS_SECRET_KEY = (
    'rRYr8iwIJhyZsBqaPrMB5x5OEgwnlEq7szt8qp5yVv1qh5UM2czjnZvS1ceeffNL'
)
DISQUS_PUBLIC_KEY = (
    'KF3jWpUzyOC6fEBJpQFUBNAX2bFreBJ4zVoZaZ3IMqPznHUw9imhYnIihQvNKkSR'
)

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
RELATIVE_URLS = True
