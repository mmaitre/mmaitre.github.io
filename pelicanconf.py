#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Marc MAITRE'
SITENAME = "NickelChromium"
SITEURL = 'http://mmaitre.github.io'

PATH = 'content'

TIMEZONE = 'Europe/Paris'


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         )

# Social widget
SOCIAL = (
        ('github', 'https://github.com/mmaitre/'),
          )

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

PLUGIN_PATHS = ['../pelican-plugins']
PLUGINS = ['i18n_subsites', 'latex']

JINJA_EXTENSIONS = ['jinja2.ext.i18n']

THEME = 'themes/notmyidea/'

DEFAULT_LANG = "en"

LOCALE = 'en_US'

I18N_SUBSITES = {
        'fr': { 
            'SITENAME': 'NickelChromium',
#LOCALE = 'fr_FR'

            },
        }


DEFAULT_CATEGORY = 'misc'

OUTPUT_SOURCES = True

languages_lookup = {
    'en': 'English',
    'fr': 'Français',
    }

def lookup_lang_name(lang_code):
    return languages_lookup[lang_code]


def my_ordered_items(dict):
    items = list(dict.items())
    # swap first and last using tuple unpacking
    items[0], items[-1] = items[-1], items[0]
    return items


JINJA_FILTERS = {
    'lookup_lang_name': lookup_lang_name,
    'my_ordered_items': my_ordered_items,
    }

STATIC_PATHS = ['images', 'files']

EXTRA_PATH_METADATA = {
    'files/.nojekyll': {
        'path': '.nojekyll',
        },
    }
