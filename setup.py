#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from setuptools import setup, find_packages
import os


CLASSIFIERS = [
    'Development Status :: 1 - Beta',
    'Environment :: Web Environment',
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: Apache License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2.5',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    'Topic :: Software Development',
    'Topic :: Software Development :: Libraries :: Application Frameworks',
]

setup(
      name='django-ajax-auth',
      author = 'Original author amenon, modified by FrancoAA',
      version = '',
      description = 'This application provides simple Django authentication via AJAX calls. To include it in your application, checkout the project and add ajax_auth to your INSTALLED_APPS. See the example project fo full usage.',
      long_description = open(os.path.join(os.path.dirname(__file__), 'README.md')).read(),
      keywords = 'django ajax auth',
      url = 'https://github.com/FrancoAA/django-ajax-auth/new/master',
      license = 'Apache v2',
      platforms = ['OS Independent'],
      classifiers = CLASSIFIERS,
      packages = find_packages(),
)
